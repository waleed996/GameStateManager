from game_state_manager.components.game_state.game_state_factory import GameStateFactory
from game_state_manager.constants import Games


class LeagueOfLegendsGameStateHelper:

    @staticmethod
    def create_test_game_state():
        """Creates an empty test game state, to be used for unit tests only"""
        # Create game state factory
        game_state_factory = GameStateFactory()
        # Get game state for game_title
        return game_state_factory.get_game_state(game_title=Games.LEAGUE_OF_LEGENDS.value)

    @staticmethod
    def initialize_test_game_state(game_state):
        """Initializes an empty game state with game state variables"""
        # game_info
        game_state.game_info = {
            'title': 'LOL_TEST',
            'match_id': 'TEST_MATCH_ID',
            'start_time': '2022-04-10T15:15:00Z',
            'series_current': 1,
            'series_max': 5,
            'series_type': 'BEST_OF',
            'match_state': None,
            'end_time': None,
            'winning_team_id': None
        }
        # players_team_mapping
        game_state.players_team_mapping = {
            'player_1': 'team_1',
            'player_2': 'team_1',
            'player_3': 'team_2',
            'player_4': 'team_2'
        }
        # team_players_list
        game_state.team_players_list = {
            'team_1': ['player_1', 'player_2'],
            'team_2': ['player_3', 'player_4']
        }
        # teams_stats
        game_state.teams_stats = {
            'team_1': {
                'dragon_kills': 0,
                'turrets_destroyed': 0
            },
            'team_2': {
                'dragon_kills': 0,
                'turrets_destroyed': 0
            }
        }
        # players_stats
        game_state.players_stats = {
            'player_1': {
                "playerID": "player_1",
                "gold": 0,
                "name": "player_1_name",
                'minion_kills': 0,
                'player_kills': 0,
                'deaths': 0,
                'assists': 0,
                'alive': True
            },
            'player_2': {
                "playerID": "player_2",
                "gold": 0,
                "name": "player_2_name",
                'minion_kills': 0,
                'player_kills': 0,
                'deaths': 0,
                'assists': 0,
                'alive': True
            },
            'player_3': {
                "playerID": "player_3",
                "gold": 0,
                "name": "player_3_name",
                'minion_kills': 0,
                'player_kills': 0,
                'deaths': 0,
                'assists': 0,
                'alive': True
            },
            'player_4': {
                "playerID": "player_4",
                "gold": 0,
                "name": "player_4_name",
                'minion_kills': 0,
                'player_kills': 0,
                'deaths': 0,
                'assists': 0,
                'alive': True
            }
        }
