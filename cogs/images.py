# teaching a bot to see
from partarutil import loadconfig,getfile
from discord.ext import commands

# load config
cfg = loadconfig("images")
corecfg = loadconfig("core")

class ImageProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def getfonts(self, ctx):
                for font in cfg["fonts"]:
                    try:
                        url = cfg["fonts"][font]["url"]
                        dest = "%s/%s" % (corecfg["filedir"], url.split("/")[-1])
                        getfile(url, dest)
                    except Exception as e:
                        await ctx.send(f"Oh no: {type(e).__name__} - {e}")
                    else:
                        await ctx.send("%s downloaded successfully." % (font))
                        
def setup(bot):
    bot.add_cog(ImageProcessor(bot))