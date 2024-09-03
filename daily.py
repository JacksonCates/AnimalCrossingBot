import discord
from discord.ext import commands, tasks
import utility
import datetime
import villager_repos
import channel_repos

channel_id = 858753397541044235

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.daily_announcements.start()    

    @tasks.loop(hours=6)
    async def daily_announcements(self):
        now = datetime.datetime.now()
        last_update = utility.get_last_update_time()

        # Is it at least a day? It is at a reasonable time?
        if now > last_update + datetime.timedelta(days=1) and now.hour > 8:

            for guild in self.bot.guilds:
                channel_id = channel_repos.get_curr_channel_id(guild.id)
                # Checks if they have registered a channels
                if channel_id is not None:
                    channel = guild.get_channel(channel_id)
                    await self.__send_villager_of_the_day(channel)
                    await self.__send_villager_birthday(channel)

            utility.save_last_update_time(now)
        
    async def __send_villager_of_the_day(self, channel: discord.channel):

        villager = await villager_repos.rand_villager()

        # Sends the bot of the day
        embed = discord.Embed(title=f"The Villager of the Day: {villager.name}", description=f"{villager.saying}", color=villager.color)
        embed = embed.set_thumbnail(url=villager.image_uri)

        await channel.send(embed=embed)

    async def __send_villager_birthday(self, channel: discord.channel):

        villagers = await villager_repos.get_villagers_birthdays_today()

        for villager in villagers:
            embed = discord.Embed(title=f"Today is {villager.name}'s birthday!!! :partying_face:", color=villager.color)
            embed = embed.set_thumbnail(url=villager.image_uri)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Daily(bot))