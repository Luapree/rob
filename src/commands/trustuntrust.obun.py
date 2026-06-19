    # /// Trust ///
    if message.content.startswith("#!trust") and message.guild:
        role = discord.utils.get(message.guild.roles, name="RobAdmin")
        if role not in message.author.roles and not message.author.guild_permissions.administrator and str(message.author.id) != str(OWNER_ID):
            await message.channel.send("...you dont have the RobAdmin role yk\ngonna need that to change my settings :3")
            return

        parts = message.content.split(maxsplit=1)

        if len(parts) != 2:
            await message.channel.send("its like #!trust <address>")
            return

        address = parts[1].strip()

        if address not in config["mailTrusted"]:
            config["mailTrusted"].append(address)
            save_config(guild_id, config)

        await message.channel.send(f"trusted `{address}` :)")
        return

    # /// Untrust ///
    if message.content.startswith("#!untrust") and message.guild:
        role = discord.utils.get(message.guild.roles, name="RobAdmin")
        if role not in message.author.roles and not message.author.guild_permissions.administrator and str(message.author.id) != str(OWNER_ID):
            await message.channel.send("...you dont have the RobAdmin role yk\ngonna need that to change my settings :3")
            return

        parts = message.content.split(maxsplit=1)

        if len(parts) != 2:
            await message.channel.send("its like #!untrust <address>")
            return

        address = parts[1].strip()

        if address in config["mailTrusted"]:
            config["mailTrusted"].remove(address)
            save_config(guild_id, config)

        await message.channel.send(f"bleh, untrusted `{address}` -_-")
        return
