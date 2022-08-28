from discord.ext import commands
from discord.utils import get

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name="witaj")
        role = get(member.guild.roles, name="Świeżak")
        await member.add_roles(role)
        await channel.send(f'Siema {member.mention}! Użyj komendy \'>weryfikacja\' i odpowiedz na kilka pytań, aby uzyskać dostęp do reszty kanałów.')
    
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     print(message)

    async def cog_load(self):
        print('Greetings ready!')

async def setup(bot):
    await bot.add_cog(Greetings(bot))