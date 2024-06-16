from redbot.core import commands, Config


class Tommybot(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1000000000)
        default_global = {
            "name": "Red-DiscordBot",
            "author": "Thomas Göttsching"
        }
        self.config.register_global(**default_global)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello World!')
