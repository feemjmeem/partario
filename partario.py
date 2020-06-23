from discord.ext import commands
import builtins
import json

# init
bot = commands.Bot(command_prefix='.')
try:
    bot.load_extension("cogs.partarutil")
except Exception as e:
    print(e)
bot.cfg = bot.get_cog("PartarioUtilityProcessor").loadconfig()
extensions = bot.cfg["core"]["extensions"]

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)

# SPIKE SENT
bot.run(bot.cfg["discord"]["token"])