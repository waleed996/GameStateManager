import json

import pytest

from game_state_manager.constants import LeagueOfLegendsEventTypes
from game_state_manager.handlers.league_of_legends.event_handler_factory import LeagueOfLegendsEventHandlerFactory
from tests.tests_league_of_legends.utils.game_state_helper import LeagueOfLegendsGameStateHelper


class TestDragonKill:
    """
    Test suite for DRAGON_KILL event
    Sample json event (Keys will always be present, values can be null)
    {
    "type": "DRAGON_KILL",
    "payload":
        {
            "killerID": "player_1",
            "dragonType": "earth",
            "goldGranted": 25
        }
    }
    """

    @pytest.fixture
    def setup(self):
        # create new game state
        self.game_state = LeagueOfLegendsGameStateHelper.create_test_game_state()
        # initialize game state
        LeagueOfLegendsGameStateHelper.initialize_test_game_state(game_state=self.game_state)
        # initialize handler
        self.event_handler = LeagueOfLegendsEventHandlerFactory().get_event_handler(event_type=LeagueOfLegendsEventTypes.DRAGON_KILL.value)

    def test_player_kills_dragon(self, setup):
        """A player kills a dragon"""

        event_json = """
            {
                "type": "DRAGON_KILL",
                "payload": {
                    "killerID": "player_1",
                    "dragonType": "earth",
                    "goldGranted": 25
                }
            }
        """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # Killer's gold should be increased to 25 (initial was 0)
        assert players_stats[killer_id]["gold"] == 25

        # Team stats Assertions
        team_id = self.game_state.players_team_mapping[killer_id]
        team_stats = self.game_state.teams_stats[team_id]

        # Teams dragon kill count should be 1 (initial was 0)
        assert team_stats["dragon_kills"] == 1

    def test_killer_id_is_null(self, setup):
        """A player kills a dragon but the killerID is null in the event"""
        event_json = """
                    {
                        "type": "DRAGON_KILL",
                        "payload": {
                            "killerID": null,
                            "dragonType": "earth",
                            "goldGranted": 25
                        }
                    }
                """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # No increase in any players gold, since we don't know who killed the dragon
        assert players_stats["player_1"]["gold"] == 0
        assert players_stats["player_2"]["gold"] == 0
        assert players_stats["player_3"]["gold"] == 0
        assert players_stats["player_4"]["gold"] == 0

        # Team Assertions
        teams_stats = self.game_state.teams_stats
        # No increase in team dragon_kills count
        assert teams_stats["team_1"]["dragon_kills"] == 0
        assert teams_stats["team_2"]["dragon_kills"] == 0

    def test_gold_granted_is_null(self, setup):
        """A player kills a dragon but goldGranted is null in the event"""
        event_json = """
                            {
                                "type": "DRAGON_KILL",
                                "payload": {
                                    "killerID": "player_1",
                                    "dragonType": "earth",
                                    "goldGranted": null
                                }
                            }
                        """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # No increase in player's gold since we don't have goldGranted in the event
        assert players_stats[killer_id]["gold"] == 0

        # Team's dragon kill count should be increased to 1
        team_id = self.game_state.players_team_mapping[killer_id]
        team_stats = self.game_state.teams_stats[team_id]
        assert team_stats["dragon_kills"] == 1

