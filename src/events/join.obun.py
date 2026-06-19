@client.event
async def on_guild_join(guild):
    config = load_config(guild.id)
    save_config(guild.id, config)
    channel = get_mail_channel(guild, config)
    if channel:
        await channel.send("hi! visit https://dogo6647.github.io/rob to learn how to set me up :)")
