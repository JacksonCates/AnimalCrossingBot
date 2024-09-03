import discord
import datetime
from discord.ext import commands

dev_id = 467169131041390592
last_update_file = "data/last_update.txt"

def get_last_update_time() -> datetime.datetime:
    # Gets the last update
    f = open(last_update_file, "r")
    string = f.readline()
    last_update = datetime.datetime.strptime(string, "%Y-%m-%d")
    f.close()
    return last_update

def save_last_update_time(now: datetime.datetime):

    # Saves the new date
    f = open(last_update_file, "w")
    f.write(now.strftime("%Y-%m-%d"))
    f.close()

def is_dev(user: discord.user):
    return user.id == dev_id

def generate_error_msg(error: commands.CommandError, usage: str, multi_name_usage: str) -> str:
    if isinstance(error, commands.MissingRequiredArgument):
        return f"Bro, you do it like this: `{usage}`"
    elif isinstance(error, commands.TooManyArguments):
        return f"Bro, you do it like this: `{usage}`. \nIf you want a villager that contains spaces, put it like this: `{multi_name_usage}`"
    elif isinstance(error, commands.MissingPermissions):
        return f"Bro, you don't have permission from me to run this"
    else:
        print(error)
        return "Oops, I'm a dump bot that cant do anything on my own. Call Jackson for halp"