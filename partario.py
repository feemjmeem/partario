from discord.ext import commands
import builtins
import json
from partarutil import loadconfig

# load config
cfg = loadconfig()
# pre-init
extensions = cfg["core"]["extensions"]

# init
bot = commands.Bot(command_prefix='.')
if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)

# SPIKE SENT
bot.run(cfg["discord"]["token"])