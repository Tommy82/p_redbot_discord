from redbot.core import commands


class Tommybot(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello World!')
