import discord
from discord.ext import commands
from discord.utils import get as dget

class IdentityProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("core")
        self.pronoun_roles = {}
        self.pronoun_roles = self.build_genders()
            
    @commands.Cog.listener()
    async def on_ready(self):
        self.pronoun_roles = self.build_genders()
        
    @commands.command()
    async def pronouns(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Who did you mean again?")
        else:
            prs = []
            for r in member.roles:
                pr = self.gpr_from_role(r, ctx.guild, self.pronoun_roles)
                if pr is not None:
                    prs.append(pr)
            pronouns = []
            if prs:
                for pr in prs:
                    pronouns.append(pr.nom)
                    pronouns.append(pr.obl)
                    pronouns.append(pr.pos)
                    pronouns.append(pr.ref)
                pronouns = list(dict.fromkeys(pronouns)) 
                op = ', '.join(pronouns)
                o = "%s's preferred pronouns are: %s." %(member.mention, op)
            else:
                o = "%s hasn't set their pronouns." % (member.mention)
            await ctx.send(o)

    def build_genders(self):
        prs = {}
        for guild in self.bot.guilds:
            gp = {}
            for pr in self.cfg["contexts"][str(guild.id)]["pronoun_roles"].items():
                r = dget(guild.roles, id=int(pr[0]))
                p = self.GenderPronounRole(role = r, guild = guild, pmap = pr[1])
                gp[str(r.id)] = p
            prs[str(guild.id)] = gp
        return(prs)
    
    def gpr_from_role(self, role: discord.Role, guild: discord.Guild, pmap: dict):
        try:
            gprs = pmap[str(guild.id)][str(role.id)]
            return(gprs)
        except:
            pass
        
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