from redbot.core import commands, Config
from redbot.core.bot import Red
import requests


class Tommybot(commands.Cog):

    def __init__(self, bot: Red, *args, **kwargs) -> None:
        # Aufruf des Parent Constructors (falls vorhanden)
        super().__init__(*args, **kwargs)
        # Registrierung des eigenen Bots
        self.bot = bot
        # Setzen der Globalen Config Datei (gültig für alle Server!)
        self.config = Config.get_conf(
            self,
            identifier=1000000,
            force_registration=True,
        )

        # Setzen der Server - Config (Wird für jeden Server neu erstellt)
        default_guild = {
            "statevkey": '--none--',
        }
        self.config.register_guild(**default_guild)


    # Kommando zum Prüfen ob der Bot gerade online ist
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello World!')

    # Setzen des API Keys für Alt:V
    # Dieser Key wird in der "guild" gespeichert, damit dieser Serverabhängig ist
    # ToDo: Rechteverwaltung einfügen
    @commands.command()
    async def addkey(self, ctx, new_key):
        await self.config.guild(ctx.guild).statevkey.set(new_key)    # Speichern des Keys in der Variable "altv_key"
        await ctx.send("Der neue State:V key wurde neu gesetzt")      # Rückmeldung an den User


    @commands.command()
    async def apitest(self, ctx):
        response = await self.getfactories(ctx)
        await ctx.send(response)

    async def getfactories(self, ctx):
        return await self.callstatev(ctx, 'factory/list/')

    async def callstatev(self, ctx, url):
        bearer_token = await self.config.guild(ctx.guild).statevkey()   # Lade altv_key
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.get("https://api.statev.de/req/" + url, headers=headers)
        return response.json()

