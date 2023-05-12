"""
Game state manager start point

League Of Legends Game State Representation dicts. All dicts are set as attributes of the LeagueOfLegendsGameState Object

game_info
{
    'title': data['payload']['fixture']['title'],
    'match_id': data['matchID'],
    'start_time': data['payload']['fixture']['startTime'],
    'series_current': data['payload']['fixture']['seriesCurrent'],
    'series_max': data['payload']['fixture']['seriesMax'],
    'series_type': data['payload']['fixture']['seriesType'],
    'match_state': 'IN_PROGRESS' || 'ENDED' etc,
    'end_time': None,
    'winning_team_id': winner_team_id
}

players_team_mapping
{
    "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed": "riot:lol:team:101383793574360315",
    ... n
}

team_players_list
{
    "riot:lol:team:101383793574360315": [
        "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed",
        "riot:lol:player:f114d45a-be6d-38a1-b163-525423d232ss",
        ... n
    ],
    "riot:lol:team:101383793574360315": [... n],
    ... n
}

teams_stats
{
    "riot:lol:team:101383793574360315": {
        'dragon_kills': 0,
        'turrets_destroyed': 0
    }, ... n
}

players_stats
{
    "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed": {
        "playerID": "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed",
        "gold": 0,
        "name": "",
        'minion_kills': 0,
        'player_kills': 0,
        'deaths': 0,
        'assists': 0,
        'alive': True
    }, ... n
}


"""

import os

from game_state_manager.components.game_state.game_state_factory import GameStateFactory
from game_state_manager.components.game_state.game_state_manager import LeagueOfLegendsGameStateManager
from game_state_manager.constants import Games

# Title of the game for which the events are to be processed
game_title = Games.LEAGUE_OF_LEGENDS.value

# Create game state factory, to be used to get game state objects for all games
game_state_factory = GameStateFactory()

# Get game state for game_title
game_state = game_state_factory.get_game_state(game_title=game_title)

# Create league of legends game state manager
lol_game_state_manager = LeagueOfLegendsGameStateManager(league_of_legends_game_state=game_state)

# consume game events
lol_game_state_manager.consume(data_path=os.getcwd() + '/league_of_legends_data/data/')

# Display Final Game State
game_state.display_game_state()
