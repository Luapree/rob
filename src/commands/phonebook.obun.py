    if message.content.startswith("#!phonebook") and message.guild:
        trusted = config.get("mailTrusted", [])

        if not trusted:
            await message.channel.send(
                "this server's phonebook is empty :(\nuse `#!trust <address>` to add servers"
            )
            return

        entries = []

        for address in trusted:
            guild_name = "unknown server"

            for guild in client.guilds:
                if guild_address(guild) == address:
                    guild_name = guild.name
                    break

            entries.append((guild_name, address))

        view = PhonebookView(entries, message.author.id)
        await message.channel.send(embed=view.make_embed(), view=view)
        return
