import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Successfully logged in!')
    print(client.user.name)
    print(client.user.id)
    print('=======')



@client.event
async def on_message(message):
    if message.content.lower().startswith('.tag'):
        await client.send_message(message.channel, "`Ƭω⚔`")


client.run ('NDczNDMzMzQ5Njg4NTI0ODAw.DkHQmw.nTosbIIt4mR_vswQTxmBMWcYTaE')
