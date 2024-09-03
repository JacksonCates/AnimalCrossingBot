from discord.ext import commands
import discord
import villager_repos
import love_calculator_repos
import joke_repos
import chat_bot
import time
import utility
import numpy.random as random

class Villagers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        pass_context=True,
        ignore_extra=False,
        help="Sends info about villagers when given a name",
        brief="Sends info about villagers"
    )
    async def profile(self, context, villager_name):

        villager = await villager_repos.get_villager_by_name(villager_name)
        if villager is None:
            await context.send(f"Bro, `{villager_name}` is not even a villager")
            return

        embed = discord.Embed(title=f"{villager.name}", description=f"{villager.saying}", color=villager.color)
        embed = embed.add_field(name="Catch-phrase", value=f"\"{villager.catch_phrase}\"", inline=True)
        embed = embed.add_field(name="Birthday", value=f"{villager.birthday}", inline=True)
        embed = embed.add_field(name="Gender", value=f"{villager.gender}", inline=True)
        embed = embed.add_field(name="Species", value=f"{villager.species}", inline=True)
        embed = embed.add_field(name="Personality", value=f"{villager.personality}", inline=True)
        embed = embed.add_field(name="Hobby", value=f"{villager.hobby}", inline=True)
        embed = embed.set_thumbnail(url=villager.image_uri)
        await context.send(embed=embed)

    @profile.error
    async def profile_error(self, context, error):
        await context.send(utility.generate_error_msg(error, "$profile <villager_name>", "$profile \"Kid Cat\""))



    # @commands.command(
    #     pass_context=True,
    #     ignore_extra=False,
    #     aliases=["love_calc"],
    #     help="Calculates the compability between two villagers",
    #     brief="Do villagers love one another?"
    # )
    # async def love(self, context, villager1_name, villager2_name):

    #     villager1 = await villager_repos.get_villager_by_name(villager1_name)
    #     if villager1 is None:
    #         await context.send(f"Bro, `{villager1_name}` is not even a villager")
    #         return
    #     villager2 = await villager_repos.get_villager_by_name(villager2_name)
    #     if villager2 is None:
    #         await context.send(f"Bro, `{villager2_name}` is not even a villager")
    #         return

    #     result = await love_calculator_repos.get_love(villager1, villager2)

    #     embed1 = discord.Embed(title=f"Does {villager1.name}", color=villager1.color)
    #     embed1 = embed1.set_thumbnail(url=villager1.image_uri)
    #     await context.send(embed=embed1)
    #     embed2 = discord.Embed(title=f"love {villager2.name}????", color=villager2.color)
    #     embed2 = embed2.set_thumbnail(url=villager2.image_uri)
    #     await context.send(embed=embed2)
    #     time.sleep(3)
    #     await context.send(f"They have a compability of {result.perc}%. {result.msg}")
    
    # @love.error
    # async def love_error(self, context, error):
    #     await context.send(utility.generate_error_msg(error, "$profile <villager1_name> <villager2_name>", "$profile \"Kid Cat\" pompom"))



    async def __send_as_villager(self, context, villager_name, message):
        villager = await villager_repos.get_villager_by_name(villager_name)
        webhook = await context.channel.create_webhook(name=villager.name)
        await webhook.send(str(message), username=villager.name, avatar_url=villager.icon_uri)
        webhooks = await context.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()



    @commands.command(
        pass_context=True,
        ignore_extra=False,
        help="Pretend to be another villager and speak for them.",
        brief="Pretend to be a villager"
    )
    async def sudo(self, context, villager_name, message):
        await self.__send_as_villager(context, villager_name, message)
        
    @sudo.error
    async def sudo_error(self, context, error):
        await context.send(utility.generate_error_msg(error, "$sudo <villager_name> <message>", "$sudo \"Kid Cat\" hi"))



    # @commands.command(
    #     pass_context=True,
    #     ignore_extra=False,
    #     help="A villager will tell you a joke.",
    #     brief="A villager will tell you a joke."
    # )
    # async def joke(self, context, villager_name = "Bob"):

    #     if villager_name.lower() == "random":
    #         villager = await villager_repos.rand_villager()
    #         villager_name = villager.name

    #     joke = await joke_repos.get_joke()
    #     # send a message for every joke
    #     for msg in joke.msgs:
    #         time.sleep(1)
    #         await self.__send_as_villager(context, villager_name, msg)

    # @joke.error
    # async def joke_error(self, context, error):
    #     await context.send(utility.generate_error_msg(error, "$joke <villager_name>", "$sudo \"Kid Cat\""))    



    # @commands.command(
    #     pass_context=True,
    #     ignore_extra=False,
    #     help="A villager will chat with you.",
    #     brief="A villager will chat with you."
    # )
    # async def chat(self, context, msg, villager_name = "Bob"):

    #     if villager_name.lower() == "random":
    #         villager = await villager_repos.rand_villager()
    #         villager_name = villager.name

    #     msg = await chat_bot.get_response(msg)
    #     # send a message for every joke
    #     await self.__send_as_villager(context, villager_name, msg)

    # @chat.error
    # async def chat_error(self, context, error):
    #     await context.send(utility.generate_error_msg(error, "$chat <msg> <villager_name>", "$sudo \"How are you?\" \"Kid Cat\""))    

def setup(bot):
    bot.add_cog(Villagers(bot))