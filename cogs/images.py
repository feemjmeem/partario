# teaching a bot to see
from discord.ext import commands

# load config

class ImageProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("images")
        self.corecfg = self.partarutil.loadconfig("core")

    # download fonts as specified in config.json
    @commands.command()
    @commands.is_owner()
    async def getfonts(self, ctx):
        for font in self.cfg["fonts"]:
            try:
                url = self.cfg["fonts"][font]["url"]
                dest = "%s/%s" % (self.corecfg["options"]["filedir"], url.split("/")[-1])
                self.partarutil.getfile(url, dest)
            except Exception as e:
                await ctx.send(f"Oh no: {type(e).__name__} - {e}")
            else:
                await ctx.send("%s downloaded successfully." % (font))
                        
def setup(bot):
    bot.add_cog(ImageProcessor(bot))