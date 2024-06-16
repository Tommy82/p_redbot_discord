from .tommybot import Tommybot


async def setup(bot):
    await bot.add_cog(Tommybot(bot))