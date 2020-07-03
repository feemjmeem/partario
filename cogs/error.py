# oh god oh fuck it broke
# error handlers for parts of the code that i haven't written correctly
import traceback
import sys
from discord.ext import commands

class ErrorProcessor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # this is messy and eventually i should handle these more locally, or add a decorator, or something
        if isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name in ["pet", "pronouns"]:
                await ctx.send("Who did you mean again?")
        
        else: # pass the error back up like we never saw it
            print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        
def setup(bot):
    bot.add_cog(ErrorProcessor(bot))