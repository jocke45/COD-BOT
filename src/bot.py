import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    """Start the bot by logging its user in"""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


"""Command functions"""


@bot.command(name='commands')
async def commands(ctx):
    """Lists the available commands"""
    await ctx.send('Available commands:')


@bot.command(name='game')
async def game(ctx, *, arg):
    """Shows the current stats for the specified users game"""
    await ctx.send('Current game stats for user ' + arg + ':')


@bot.command(name='stats')
async def stats(ctx, *, arg):
    """Shows the recent stats for the specified user"""
    await ctx.send('Stats for user ' + arg + ':')


@bot.command(name='wins')
async def wins(ctx, *, arg):
    """Shows the recent stats for the specified user"""
    await ctx.send(arg + ' has x number of wins!')


"""Error handling functions"""


@game.error
async def game_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a user ID')


@stats.error
async def stats_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a user ID')


@wins.error
async def wins_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a user ID')


bot.run(config.bot_api_key)
