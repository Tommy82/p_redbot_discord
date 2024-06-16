from redbot.core import commands, Config
from redbot.core.bot import Red


class Tommybot(commands.Cog):
    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=1000000,
            force_registration=True,
        )
        default_guild = {
            "manager": [],
            "guessing_time": 60,
            "voting_time": 60,
        }
        self.config.register_guild(**default_guild)
        self.cache = {}

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello World!')

