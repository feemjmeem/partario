# partario's cpu is a neural net processor: a learning computer
import discord
from builtins import cfg
from discord.ext import commands

class NeuralNetProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def pet(self, ctx, member: discord.Member = None):
    # who now?
        giver = ctx.author
        if member == giver:
            o = "*stares at %s and shakes his head.*" % (giver.mention)
        elif member == self.bot.user:
            o = "*shrugs and pats himself on the head.*"
        elif member:
            o = "*glances between %s and %s uncomfortably.*" % (giver.mention, member.mention)
        else:
            o = "*looks around, then shrugs.*"
        await ctx.send(o)
        
    @commands.command()
    async def feem(self, ctx):
        await ctx.send("who the fuck is feem")
        
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            if cog == "all":
                cog = cfg["core"]["extensions"]
                # figure out how to only specify unload/load once for both cases
                for c in cog:
                    self.bot.unload_extension(c)
                    self.bot.load_extension(c)
            else:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog) 
        except Exception as e:
            await ctx.send(f"Oh no: {type(e).__name__} - {e}")
        else:
            await ctx.send("i deed it")
    
def setup(bot):
    bot.add_cog(NeuralNetProcessor(bot))