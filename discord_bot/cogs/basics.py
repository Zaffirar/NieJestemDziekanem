from discord.ext import commands


class Basics(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def Siema(self, ctx):
        await ctx.send(f"Siema {ctx.message.author}!")

    async def cog_load(self):
        print('Basics ready!')


async def setup(bot):
    await bot.add_cog(Basics(bot))
