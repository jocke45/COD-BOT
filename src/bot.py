import discord
from discord.ext import commands
import config
import get_data
import handle_data

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
    embed = discord.Embed()
    embed.add_field(name='Available commands',
                    value='**!help** - display help message\n'
                          '**!commands** - display this message\n'
                          '**!level** user_id - display the level of the specified player\n'
                          '**!stats** user_id - display stats for the specified player\n'
                          '**!wins** user_id - how many times has this player eaten chicken dinner?',
                    inline=False)
    await ctx.send(embed=embed)


@bot.command(name='level')
async def level(ctx, *, arg):
    """Shows the current level for the specified player"""
    await ctx.send(embed=handle_data.get_level_embed(arg))


@bot.command(name='stats')
async def stats(ctx, *, arg):
    """Shows selected stats for the specified player"""
    await ctx.send(embed=handle_data.get_stats_embed(arg))


@bot.command(name='wins')
async def wins(ctx, *, arg):
    """Shows the recent stats for the specified player"""
    await ctx.send(embed=handle_data.get_wins_embed(arg))


"""Error handling functions"""


@level.error
async def level_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a player ID')


@stats.error
async def stats_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a player ID')


@wins.error
async def wins_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Please specify a player ID')


bot.run(config.bot_api_key)
