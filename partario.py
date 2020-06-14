import json
import html
from datetime import datetime

import discord
from discord.ext import commands

import googleapiclient.discovery

# load config
with open("config.json", "r") as cfg_json:
    cfg = json.load(cfg_json)

# initialize partario bot
pt = commands.Bot(command_prefix='.')

# initialize youtube api
youts = googleapiclient.discovery.build(
    "youtube",
    "v3",
    developerKey = cfg["youtube"]["token"]
)

# youtube search
@pt.command()
async def yt(ctx, *args):
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
    # it's better than bad, it's good
    print(o)
    # SEND SPIKE
    await ctx.send(o)

@pt.command()
async def pet(ctx, member: discord.Member = None):
    # who now?
    giver = ctx.author
    if member == giver:
        o = "*stares at %s and shakes his head.*" % (giver.mention)
    elif member == pt.user:
        o = "*shrugs and pats himself on the head.*"
    elif member:
        o = "*glances between %s and %s uncomfortably.*" % (giver.mention, member.mention)
    else:
        o = "*looks around, then shrugs.*"
    await ctx.send(o)

@pt.command()
async def feem(ctx):
    await ctx.send("who the fuck is feem")

# SPIKE SENT
pt.run(cfg["discord"]["token"])
