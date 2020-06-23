import json
import requests
from os import path
from discord.ext import commands

class PartarioUtilityProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def loadconfig(self, part = None):
        with open("config.json", "r") as cfg_json:
            cfg = json.load(cfg_json)
            if part:
                try:
                    return(cfg[part])
                except Exception as e:
                    print(f"POOH THAT'S NOT CONFIG.JSON YOU'RE EATING: {type(e).__name__} - {e}" )
            else:
                return(cfg)

    def getfile(self, url = None, dest = None, force = False):
        if (url is None) or (dest is None):
            raise ValueError("getfile: both url and dest are required")
        else:
            if not path.exists(dest) or force == True:
                grabby = None
                try:
                    print("Attempting download of %s..." % url)
                    grabby = requests.get(url, allow_redirects = True)
                except:
                    raise ValueError("aw hell download of %s failed" % (url))
                try:
                    print("Download of %s complete." % url)
                    open(dest, "wb").write(grabby.content)
                except:
                    raise ValueError("aw hell i couldn't write %s" % (dest))
            else:
                raise ValueError("aw hell %s is already present (use force=True to override)" % dest)

def setup(bot):
    bot.add_cog(PartarioUtilityProcessor(bot))