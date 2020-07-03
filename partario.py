from discord.ext import commands

# init
bot = commands.Bot(command_prefix='.') # what do we listen to?
try:
    bot.load_extension("cogs.partarutil") # we need this to load json
except Exception as e:
    print(e)
bot.cfg = bot.get_cog("PartarioUtilityProcessor").loadconfig()
extensions = bot.cfg["core"]["extensions"]

# loop to load all configured cogs on init
if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)

# SPIKE SENT
bot.run(bot.cfg["discord"]["token"])