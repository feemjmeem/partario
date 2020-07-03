# for some reason there's a twitter module now
import tweepy
from urlextract import URLExtract
from discord.ext import commands

class TwitterProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.partarutil = self.bot.get_cog("PartarioUtilityProcessor")
        self.cfg = self.partarutil.loadconfig("twitter")
        
        # set up twitter handle 
        auth = tweepy.OAuthHandler(self.cfg["consumer"]["token"], self.cfg["consumer"]["secret"])
        auth.set_access_token(self.cfg["access"]["token"], self.cfg["access"]["secret"])
        self.twits = tweepy.API(auth)

    # listen for a tweet, check if the tweet is a quote/retweet, and post the original tweet.
    # this listens to itself too, so it can follow retweet chains.
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
            
            tweet = self.twits.get_status(tid, tweet_mode="extended")
            try:
                o = "⬆ retweet of %s ⬆" % (tweet.quoted_status_permalink["expanded"])
                await message.channel.send(o)
            except:
                pass
             
def setup(bot):
    bot.add_cog(TwitterProcessor(bot))