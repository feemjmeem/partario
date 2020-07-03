import discord
from discord.ext import commands
from discord.utils import get as dget

class IdentityProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("core")
        # initialize pronoun_roles empty dict and populate on reload of cog
        self.pronoun_roles = {}
        self.pronoun_roles = self.build_genders()
            
    @commands.Cog.listener()
    async def on_ready(self):
        # the first time we start up, we have to wait for the handle to open before we can populate this
        self.pronoun_roles = self.build_genders()
    
    # get pronouns via the pronoun roles associated with a user    
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
           
    # set or unset pronouns based upon pronoun roles defined in config.json
    @commands.command()
    async def mypronouns(self, ctx, selector: str = None):
        o = None
        op = 1
        if "-" in selector:
            op = 0
            selector = selector.replace("-", "")
        if selector is not None:
            member = ctx.message.author
            proles = {}
            g = ctx.guild
            guild_pronouns = self.pronoun_roles[str(g.id)]
            for r in guild_pronouns:
                p = guild_pronouns[r]["nom"]
                proles[p] = r
            gr = proles.get(selector, None)
            if gr is not None:
                try:
                    role = dget(g.roles, id=int(gr))
                    if op:
                        await member.add_roles(role)
                        o = "%s have been added to your pronouns, %s" % (role.name, member.mention)
                    else:
                        await member.remove_roles(role)
                        o = "%s have been removed from your pronouns, %s" % (role.name, member.mention)
                except Exception as e:
                    print(e)
                    o = "Hmm. I'm confused. Try again."
            else:
                o = "Hmm. I can't find that pronoun. Try again using the nominative pronoun on its own (i.e. she, they, he)."
        else:
            o = "Which pronouns did you want to set? Try using the nominative pronoun on its own (i.e she, they, he)."
        await ctx.send(o)

    # abstract reload of pronoun roles from config.json
    def build_genders(self):
        prs = {}
        for g in self.bot.guilds:
            prs[str(g.id)] = self.cfg["contexts"][str(g.id)]["pronoun_roles"]
        return(prs)
    
def setup(bot):
    bot.add_cog(IdentityProcessor(bot))