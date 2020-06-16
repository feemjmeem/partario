import json

def loadconfig(part = None):
    with open("config.json", "r") as cfg_json:
        cfg = json.load(cfg_json)
        if part:
            try:
                return(cfg[part])
            except Exception as e:
                print(f"POOH THAT'S NOT CONFIG.JSON YOU'RE EATING: {type(e).__name__} - {e}" )
        else:
            return(cfg)