from discord.ext import commands
import builtins
import json

# load config
with open("config.json", "r") as cfg_json:
    cfg = json.load(cfg_json)
    
# pre-init
builtins.cfg = cfg
extensions = cfg["core"]["extensions"]

# init
bot = commands.Bot(command_prefix='.')
if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)

# SPIKE SENT
bot.run(cfg["discord"]["token"])