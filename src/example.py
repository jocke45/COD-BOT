import discord
import config

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        # Do not respond to our own message
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('!help'):
        await message.channel.send('**Help:**')
        await message.channel.send('> !help - display this help message')
        await message.channel.send('> !commands - list all available commands')
        await message.channel.send('> !game *user_id* - list stats for the specified user IDs current game')
    elif message.content.startswith('!commands'):
        await message.channel.send('**Available commands**')
        await message.channel.send('> !commands - list all available commands')
        await message.channel.send('> !help - display a help message')
        await message.channel.send('> !game - list stats from a specified user IDs current game')

client.run(config.bot_api_key)
