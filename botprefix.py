import json

def prefix(bot, ctx):
    with open("./prefix.json", "r") as f:
        prefixes = json.load(f)
        id = str(ctx.guild.id)
        default_prefix = prefixes["default_prefix"]
    return prefixes.get(id, default_prefix)