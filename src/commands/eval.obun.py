    if message.content.startswith("#!eval") and message.author.id == OWNER_ID:
        await message.channel.send(exec(message.content.replace('#!eval ', '')))
