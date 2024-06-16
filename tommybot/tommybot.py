from redbot.core import commands, Config


class Tommybot(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        self.config.register_global(
            foo=True
        )

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello World!')
        await ctx.send(await self.config.foo())

