

@tasks.loop(hours=6)
async def daily_announcements():

    now = datetime.datetime.now()
    last_update = get_last_update_time()

    # Is it at least a day? It is at a reasonable time?
    if now > last_update + datetime.timedelta(days=1) and now.hour > 8:
        
        id = random.randint(391)

        # Sends the API call
        response = requests.get(f"http://acnhapi.com/v1/villagers/{id}")
        if response.status_code != 200:
            await client.get_channel(channel_id).send("Oops, I'm a dum bot that can't do anything on my own, get Jackson for Halp")
            return

        json = response.json()
        name = json["name"]["name-USen"]
        saying = json["saying"]
        color = int(json["bubble-color"][1:], 16)
        dob = json["birthday-string"]
        species = json["species"]
        hobby = json["hobby"]
        catch_phrase = json["catch-phrase"]
        gender = json["gender"]
        icon_url = json["image_uri"]
        personality = json["personality"]

        # Sends the bot of the day
        embed = discord.Embed(title=f"The Villager of the Day: {name}", description=f"{saying}", color=color)
        embed = embed.add_field(name="Catch-phrase", value=f"\"{catch_phrase}\"", inline=True)
        embed = embed.add_field(name="Birthday", value=f"{dob}", inline=True)
        embed = embed.add_field(name="Gender", value=f"{gender}", inline=True)
        embed = embed.add_field(name="Species", value=f"{species}", inline=True)
        embed = embed.add_field(name="Personality", value=f"{personality}", inline=True)
        embed = embed.add_field(name="Hobby", value=f"{hobby}", inline=True)
        embed = embed.set_thumbnail(url=icon_url)
        await client.get_channel(channel_id).send(embed=embed)

        save_last_update_time(now)
        