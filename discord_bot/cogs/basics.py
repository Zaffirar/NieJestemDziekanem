from discord.ext import commands
import random

vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'A', 'E', 'I', 'O', 'Ó', 'U']


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

# from https://github.com/Zenrac/TextToOwO/blob/master/TextToOwO/owo.py
def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text


class Basics(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def Siema(self, ctx):
        await ctx.send(f"Siema {ctx.message.author}!")

    @commands.command()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content[4:]))

    async def on_ready(self):
        print('Basics ready!')


async def setup(bot):
    await bot.add_cog(Basics(bot))
