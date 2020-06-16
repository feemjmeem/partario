# for some reason there's a twitter module now
import tweepy
from urlextract import URLExtract
from partarutil import loadconfig
from discord.ext import commands

# load config
cfg = loadconfig("twitter")

# initialize twitter api
auth = tweepy.OAuthHandler(cfg["consumer"]["token"], cfg["consumer"]["secret"])
auth.set_access_token(cfg["access"]["token"], cfg["access"]["secret"])
twits = tweepy.API(auth)

class TwitterProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if "twitter.com" in message.content:
            extractor = URLExtract()
            urls = extractor.find_urls(message.content)
            if "?" in urls[0]:
                tid = urls[0].split("?")[0]
            else:
                tid = urls[0]
            tid = tid.split("/")[-1]
            
            tweet = twits.get_status(tid, tweet_mode="extended")
            try:
                o = "⬆ retweet of %s ⬆" % (tweet.quoted_status_permalink["expanded"])
                await message.channel.send(o)
            except:
                pass
             
def setup(bot):
    bot.add_cog(TwitterProcessor(bot))