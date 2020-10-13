import discord
import json
import get_data

# Get the data we are going to handle
data: dict = get_data.get_data()


def get_best_aim(player):
    """"""
    return data


def get_level(player):
    """Returns player level as a float"""
    return data['level']


def get_stats(player):
    """Get certain stats for the player"""
    # TODO
    return "not done"


def get_suicides(player):
    """Return number of suicides for the player as a float"""
    return data['lifetime']['all']['properties']['suicides']


def get_wins(player):
    """Return number of wins for the player as a float"""
    return data['lifetime']['mode']['br']['properties']['wins']


def get_level_embed(player):
    player_level = str(int(get_level(player)))
    embed = discord.Embed()
    embed.add_field(name='Level', value='Player ' + player + ' is level ' + player_level, inline=True)
    return embed


def get_stats_embed(player):
    player_stats = get_stats(player)
    embed = discord.Embed()
    embed.add_field(name='Stats', value=player + ' is level ' + player_stats, inline=True)
    return embed


def get_wins_embed(player):
    player_wins = str(int(get_wins(player)))
    player_suicides = str(int(get_suicides(player)))
    embed = discord.Embed()
    embed.add_field(name='Wins', value='Player ' + player + ' has won ' + player_wins + ' times!\n They also suicided '
                                       + player_suicides + ' times...',
                    inline=True)
    return embed


print(data['lifetime']['all']['properties']['suicides'])
