from game_state_manager.constants import LeagueOfLegendsSeriesMatchStates
from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class MatchStartEventHandler(LeagueOfLegendsEventHandler):
    """
    Game State Representation dicts

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

    def handle(self, data, game_state):
        """
        Handles the MATCH_START event, initialize game state with all game, player and team counts information
        :param data: (dict) event data in dict type
        :param game_state: (LeagueOfLegendsGameState) game state object
        :return: None
        """

        # Processing the start event and creating dicts for player and team stats
        # This would help in accessing player and team information in constant time using their dictionary, instead of
        # looping over the players list every time a player count needs to be updated

        # Information about the game
        game_info = {
            'title': data['payload']['fixture']['title'],
            'match_id': data['matchID'],
            'start_time': data['payload']['fixture']['startTime'],
            'series_current': data['payload']['fixture']['seriesCurrent'],
            'series_max': data['payload']['fixture']['seriesMax'],
            'series_type': data['payload']['fixture']['seriesType'],
            'match_state': LeagueOfLegendsSeriesMatchStates.IN_PROGRESS.value,
            'end_time': None,
            'winning_team_id': None
        }

        # playerID - teamID mappings for all players of all teams
        players_team_mapping = dict()

        # teamID and list of playerIDs
        team_players_list = dict()

        # all teams and their team stats
        teams_stats = dict()

        # all players and their stats
        players_stats = dict()
        for team in data["payload"]["teams"]:
            for player_info in team['players']:

                # Add playerID-teamID mapping
                players_team_mapping[player_info["playerID"]] = team["teamID"]

                # Add teamID-playerIDs list mapping
                if team_players_list.get(team["teamID"]):
                    team_players_list[team["teamID"]].append(player_info["playerID"])
                else:
                    team_players_list[team["teamID"]] = [player_info["playerID"]]

                # Player stats that need to be tracked
                player_stats_to_track = {
                    'minion_kills': 0,
                    'player_kills': 0,
                    'deaths': 0,
                    'assists': 0
                }
                player_stats_to_track.update(player_info)
                players_stats[player_info["playerID"]] = player_stats_to_track

            # Team stats that need to be tracked
            teams_stats[team["teamID"]] = {
                'dragon_kills': 0,
                'turrets_destroyed': 0
            }

        # Initialize the empty game state
        game_state.initialize(game_info=game_info, players_team_mapping=players_team_mapping, teams_stats=teams_stats,
                              players_stats=players_stats, team_players_list=team_players_list)
