# teaching a bot to see
from partarutil import loadconfig
from discord.ext import commands

# load config
cfg = loadconfig("images")

class ImageProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(ImageProcessor(bot))