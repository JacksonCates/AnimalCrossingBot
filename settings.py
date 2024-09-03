import discord
from discord.ext import commands
import utility
import channel_repos

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        pass_context=True,
        help="Sends the time when the bot last checked daily updates",
        brief="Sends time last updated"
    )
    async def last_update(self, context):
        if utility.is_dev(context.message.author):
            await context.channel.send(f"The last update was on `{utility.get_last_update_time()}`")


    @commands.command(
        pass_context=True,
        help="Sets the channel for announcements to be made. Only people with the role of administrator can call this command.",
        brief="Sets channel announcements"
    )
    async def set_channel(self, context):
        if utility.is_dev(context.message.author):
            choice_dict = {}
            i = 0
            msg = "Select a channel to send announcements. Type \"cancel\" to exit."
            for channel in context.guild.text_channels:
                choice_dict[i] = channel.id
                msg += f"\n{channel} - {i}"
                i += 1
            await context.channel.send(msg)

            try:
                msg = await self.bot.wait_for("message", check=lambda message: message.author == context.author, timeout=30.0)
            except:
                await context.channel.send("Too slow sucker!")

            choice = msg.content

            # Checks choice
            try:
                if choice == "cancel":
                    await context.channel.send("Ok bye")
                    return
                elif int(choice) not in choice_dict:
                    raise Exception()
            except:
                await context.channel.send("Bro thats not even a channel. Run the command again.")
                return 

            choice = int(choice)
            channel_repos.add_channel(context.guild.id, choice_dict[choice]) 
            await context.channel.send("Added boss")

    @commands.command(
        pass_context=True,
        help="Views the channel for announcements to be made. Only people with the role of administrator can call this command.",
        brief="View channel announcement"
    )
    async def view_channel(self, context):
        if utility.is_dev(context.message.author):
            channel_id = channel_repos.get_curr_channel_id(context.guild.id)
            channel = context.guild.get_channel(channel_id)
            await context.channel.send(f"The current channel where announcements are made is at `{channel}`")

def setup(bot):
    bot.add_cog(Settings(bot))