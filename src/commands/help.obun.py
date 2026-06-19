    if message.content.startswith("#!help") and message.guild:
        await message.channel.send("heres th my options you can change :)")
        await message.channel.send(f"{'\n'.join(config.keys())} \n\nuse the `#!option <option> <value>` command to change them")
        await message.channel.send("youre gonna need the RobAdmin role tho...")
