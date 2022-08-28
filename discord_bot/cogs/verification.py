from discord.ext import commands
from discord.utils import get
import json
import requests


class Utils:
    def __init__(self):
        # {discord_member -> [http_questions, iterator, current_question]}
        self._dict = {}

    def add_person(self, person, questions):
        if person not in self._dict:
            iterator = iter(questions)
            self._dict[person] = [questions, iterator, next(iter(iterator))]

    def person_has_questions(self, person):
        return person in self._dict

    def get_question(self, person):
        current_question = self._dict[person][2]
        current_answers = self._dict[person][0][current_question]
        return (current_question, current_answers)

    def answer_is_valid(self, person, answer):
        current_question = self._dict[person][2]
        current_answers = self._dict[person][0][current_question]
        return current_answers is None or answer in current_answers

    def save_answer_and_check_if_that_was_last_question(self, person, answer):
        current_question = self._dict[person][2]
        self._dict[person][0][current_question] = answer
        try:
            self._dict[person][2] = next(self._dict[person][1])
        except StopIteration:
            return True
        return False

    def get_person_answers_and_member(self, person):
        for member, [answers, _, _] in self._dict.items():
            if member == person:
                return answers, member

    def remove_person(self, person):
        self._dict.pop(person)


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wrapper = Utils()

    @commands.command()
    @commands.has_role("Świeżak")
    async def weryfikacja(self, ctx):
        if ctx.channel.name != "witaj":
            await ctx.send("Ta komenda działa tylko na kanale \'witaj\'")
            return
        requester = ctx.author
        channel = requester.dm_channel
        if channel is None:
            channel = await requester.create_dm()
        await channel.typing()
        questions_json = requests.get(
            "http://127.0.0.1:5000/questions").json()
        self.wrapper.add_person(requester, questions_json)
        question, answers = self.wrapper.get_question(requester)
        await channel.send(f'{requester.name}, chciałeś weryfikację, to masz!')
        await channel.send(f'Za chwilę zadam ci po kolei 13 pytań. Część będzie otawrta, część zamknięta. Odpowiadaj zgodnie z twoją wiedzą (Trust me bro!).')
        await channel.send(f'Odpowiedz na pytanie: \"{question}\"')
        if answers is not None:
            msg = f'Możliwe odpowiedzi: {answers}'
            await channel.send(msg.replace("\'", ""))
        else:
            await channel.send('Jeżeli nie znasz odpowiedzi na pytanie, odpowiedz \'nie wiem\'')
        await channel.send('Odpowiedź zacznij od komendy \">odp \"')

    @commands.command()
    @commands.dm_only()
    async def odp(self, ctx):
        await ctx.typing()
        requester = ctx.author
        if not self.wrapper.person_has_questions(requester):
            await ctx.send('Najpierw rozpocznij weryfikację przy pomocy komendy \">weryfikacja\"')
            return
        dm_channel = requester.dm_channel
        if dm_channel is None:
            dm_channel = await requester.create_dm()
        ans = ctx.message.content[4:].strip()
        if self.wrapper.answer_is_valid(requester, ans):
            if self.wrapper.save_answer_and_check_if_that_was_last_question(requester, ans):
                await dm_channel.send('To było ostatnie pytanie, rozpoczynam weryfikację odpowiedzi!')
                await self.run_verification(requester, dm_channel)
                return
        else:
            await dm_channel.send(f'Odpowiedzi \'{ans}\' nie ma w możliwych odpowiedziach! Spróbuj ponownie.')
        question, answers = self.wrapper.get_question(requester)
        await dm_channel.send(f'Odpowiedz na pytanie: \"{question}\"')
        if answers is not None:
            msg = f'Możliwe odpowiedzi: {answers}'
            await dm_channel.send(msg.replace("\'", ""))
        else:
            await dm_channel.send('Jeżeli nie znasz odpowiedzi na pytanie, odpowiedz \'nie wiem\'')
        await dm_channel.send('Odpowiedź zacznij od komendy \">odp \"')

    async def run_verification(self, user, dm_channel):
        ans, member = self.wrapper.get_person_answers_and_member(user)
        result = requests.post("http://127.0.0.1:5000/answers", json=ans)

        if result.text == "True":
            student_role = get(member.guild.roles, name="Student")
            swiezak_role = get(member.guild.roles, name="Świeżak")
            await member.add_roles(student_role)
            await member.remove_roles(swiezak_role)
            await dm_channel.send("Pomyślnie przeszedłeś weryfikację, gratulacje! Teraz zostanie ci nadana ranga Studenta.")
        elif result.text == "False":
            swiezak_role = get(member.guild.roles, name="Świeżak")
            await member.remove_roles(swiezak_role)
            await dm_channel.send("Nie tym razem panie dziekan! (Jeżeli nie jesteś pracownikiem uczelni to napisz do admina)")
        else:
            await dm_channel.send("Coś poszło nie tak, próbuj ponownie używając \'>weryfikacja\' na kanale witaj")

        self.wrapper.remove_person(member)

    async def cog_load(self):
        print('Verification ready!')


async def setup(bot):
    await bot.add_cog(Verification(bot))
