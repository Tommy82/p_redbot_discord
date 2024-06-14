#from discord.ext import tasks
from redbot.core import Config, commands
from redbot.core.config import Config
import aiohttp
import json
import discord

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

        #Erstellung der Config / identitfier ist Eindeutig diesem Cog zuzuordnen
        self.config = Config.get_conf(self, identifier=1234567890)      
        
        #Globalen Einstellungen - Serverübergreifend !!!
        default_global = {                                              
            "name": "RedBot",
            "author": "Thomas Göttsching"
        }
        self.config.register_global(**default_global)

        #Servereinstellungen - Gilt nur für den jeweiligen Server (GUILDID = ServerID)
        default_guild = {                                               
            "statevtoken": ""
        }
        self.config.register_guild(**default_guild)
        self.config.name.set("Tommy´s RedBot")
        self.config.author.set("Thomas Göttsching")


    #Command - Ein kurzes Hallo vom Bot
    @commands.command()
    async def hello(self, ctx):
        author = self.config.author                                                                             #Laden des Authors aus der Config
        name = self.config.name                                                                                 #Laden des Namens aus der Config
        await ctx.send(("Hello from {botname} created by {author}!").format(botname=name, author=author))       #Rückgabe


    #Command - Ändern des StateV Tokens
    #Permission: Nur der Servereigentümer kann das ändern
    @commands.command()
    @commands.is_owner()
    async def addToken(self, ctx, new_value):
        await self.config.guild(ctx.guild).statevtoken.set(new_value)                                           #Setzen des Tokens
        await ctx.send('StateV Token changed')                                                                  #Rückgabe


    #Laden aller Member von einem Server
    async def getMembersOfGuild(self, guild: discord.Guild):
        response = []
        #wenn Server nicht vorhanden, breche Funktion ab
        if guild is None:
            return response
        #schreibe alle Member in eine Liste
        for member in guild.members:
            response.append(member)
        return response

    @commands.command()
    async def getMembers(self, ctx):
        guild: discord.Guild = ctx.guild
        members = await self.getMembersOfGuild(guild)
        for member in members:
            await ctx.send(member)
            await ctx.send(member.guild)
