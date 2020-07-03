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
        if member:
            pronouns = []
            g = ctx.guild
            guild_pronouns = self.pronoun_roles[str(g.id)]
            for r in member.roles:
                try:
                    ps = guild_pronouns[str(r.id)]
                    for p in ps.values():
                        pronouns.append(p)
                except:
                    pass
            if pronouns:
                o = "%s's preferred pronouns are: %s" % (member.mention, ', '.join(pronouns))
            else:
                o = "%s has not selected preferred pronouns." % (member.mention)
            await ctx.send(o)
            
    def build_genders(self):
        prs = {}
        for g in self.bot.guilds:
            prs[str(g.id)] = self.cfg["contexts"][str(g.id)]["pronoun_roles"]
        return(prs)
    
    def build_pronouns(self, guild: discord.Guild):
        prs = self.pronoun_roles[str(guild.id)]
        pdict = {}
        for r in prs:
            ps = list(prs[r].values())
            pdict[str(r)] = ps
        return(pdict)
    
def setup(bot):
    bot.add_cog(IdentityProcessor(bot))