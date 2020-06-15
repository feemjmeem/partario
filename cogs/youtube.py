# he can do the youtubes
import html
import googleapiclient.discovery
from builtins import cfg
from datetime import datetime
from discord.ext import commands

# initialize youtube api
youts = googleapiclient.discovery.build(
    "youtube",
    "v3",
    developerKey = cfg["youtube"]["token"]
)

class YoutubeProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # youtube search
    @commands.command()
    async def yt(self, ctx, *args):
        # form query, limiting fields to what we're going to use
        query = youts.search().list(
            part="snippet",
            maxResults=1,
            q=" ".join(args[:]),
            fields="items(id(videoId),snippet(title,channelTitle,publishedAt))"
        )
        r = query.execute()
        # form output
        o = "https://youtube.com/watch?v=%s [%s] date[%s] author[%s]" % (
            r["items"][0]["id"]["videoId"],
            html.unescape(r["items"][0]["snippet"]["title"]),
            datetime.strptime(r["items"][0]["snippet"]["publishedAt"],"%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d"),
            html.unescape(r["items"][0]["snippet"]["channelTitle"]))
        await ctx.send(o)

def setup(bot):
    bot.add_cog(YoutubeProcessor(bot))