from wikipedia import wikipedia
from discord.ext import commands

class WikiProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("wikipedia")       
    
    # perform a wikipedia search and return an article    
    @commands.command()
    async def w(self, ctx, *, sq: str):
        try:
            s = wikipedia.search(sq, results=1)
        except Exception:
            await ctx.send("I didn't find anything.")
        else:
            try:
                p = wikipedia.page(s)
            except Exception:
                await ctx.send("Hmm. Can you be more a little more specific?")
            else:
                await ctx.send(p.url)
        
def setup(bot):
    bot.add_cog(WikiProcessor(bot))