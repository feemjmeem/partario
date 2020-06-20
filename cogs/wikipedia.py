from discord.ext import commands
from partarutil import loadconfig

cfg = loadconfig("wikipedia")

class WikiProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
def setup(bot):
    bot.add_cog(WikiProcessor(bot))