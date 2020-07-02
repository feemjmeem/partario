import discord
from discord.ext import commands
from discord.utils import get as dget

class IdentityProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("core")
        self.pronoun_roles = {}
            
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            gp = {}
            for pr in self.cfg["contexts"][str(guild.id)]["pronoun_roles"].items():
                r = dget(guild.roles, id=int(pr[0]))
                p = self.GenderPronounRole(role = r, guild = guild, pmap = pr[1])
                gp[str(r.id)] = p
            self.pronoun_roles[str(guild.id)] = gp
        
    @commands.command()
    async def lp(self, ctx):
        g = ctx.message.guild.id
        prr = []
        for p in self.pronoun_roles[str(g)]:
            pr = self.pronoun_roles[str(g)][str(p)]
            prr.append(vars(pr))
        await ctx.send(prr)
         
    class GenderPronounRole():
        def __init__(self, role: discord.Role, guild: discord.Guild, pmap: dict):
            self.role = role 
            self.guild = guild
            self.nom = pmap["nom"]
            self.obl = pmap["obl"]
            self.pos = pmap["pos"]
            self.ref = pmap["ref"]
                
def setup(bot):
    bot.add_cog(IdentityProcessor(bot))