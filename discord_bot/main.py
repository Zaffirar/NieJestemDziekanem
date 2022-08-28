from discord import Intents
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix='>', intents=intents)
        self.initial_extensions = [
            'cogs.basics',
            'cogs.verification',
            'cogs.greetings'
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def close(self):
        await super().close()

    async def on_ready(self):
        print('Bot ready!')


bot = MyBot()
bot.run('')
