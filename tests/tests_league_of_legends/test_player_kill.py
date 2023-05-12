import json
import pytest

from game_state_manager.constants import LeagueOfLegendsEventTypes
from game_state_manager.handlers.league_of_legends.event_handler_factory import LeagueOfLegendsEventHandlerFactory
from tests.tests_league_of_legends.utils.game_state_helper import LeagueOfLegendsGameStateHelper


class TestPlayerKill:
    """
    Test suite for PLAYER_KILL event
    Sample json event (Keys will always be present, values can be null)
    {
    "type": "PLAYER_KILL",
    "payload":
        {
            "killerID": "player_1",
            "victimID": "player_3",
            "goldGranted": 600,
            "assistants": [
                "player_2"
            ],
            "assistGold": 150
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
        self.event_handler = LeagueOfLegendsEventHandlerFactory().get_event_handler(event_type=LeagueOfLegendsEventTypes.PLAYER_KILL.value)

    def test_player_kills_another_player_with_assistants(self, setup):
        """A player kills another player with help from his team members"""
        event_json = """
        {
            "type": "PLAYER_KILL",
            "payload":
                {
                    "killerID": "player_1",
                    "victimID": "player_3",
                    "goldGranted": 600,
                    "assistants": [
                        "player_2"
                    ],
                    "assistGold": 150
                }
            }
        """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 600 (original value 0)
        assert players_stats[killer_id]["gold"] == 600
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

        # Kill Assistants assertions
        assistant_id = event_dict["payload"]["assistants"][0]
        # assists should be 1
        assert players_stats[assistant_id]["assists"] == 1
        # gold should be 150
        assert players_stats[assistant_id]["gold"] == 150

    def test_player_kills_another_player_without_assistants(self, setup):
        """A player kills another player without assist"""
        event_json = """
        {
            "type": "PLAYER_KILL",
            "payload":
                {
                    "killerID": "player_1",
                    "victimID": "player_3",
                    "goldGranted": 600,
                    "assistants": [],
                    "assistGold": 150
                }
            }
        """
        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 600 (original value 0)
        assert players_stats[killer_id]["gold"] == 600
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

        # Kill Assistants assertions

        # assists of player_2 and player_4 should be 0
        assert players_stats['player_2']['assists'] == 0
        assert players_stats['player_4']['assists'] == 0

        # player kills should be 0
        assert players_stats['player_2']['player_kills'] == 0
        assert players_stats['player_4']['player_kills'] == 0

        # their gold should be still 0
        assert players_stats['player_2']['gold'] == 0
        assert players_stats['player_4']['gold'] == 0

        # their deaths should be still 0
        assert players_stats['player_2']['deaths'] == 0
        assert players_stats['player_4']['deaths'] == 0

        # they should be still alive
        assert players_stats['player_2']['alive'] is True
        assert players_stats['player_4']['alive'] is True

    def test_player_kills_another_player_assistants_is_null(self, setup):
        """A player kills another player without assistants but the assistants is null instead of []"""
        event_json = """
                {
                    "type": "PLAYER_KILL",
                    "payload":
                        {
                            "killerID": "player_1",
                            "victimID": "player_3",
                            "goldGranted": 600,
                            "assistants": null,
                            "assistGold": 150
                        }
                    }
                """
        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 600 (original value 0)
        assert players_stats[killer_id]["gold"] == 600
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

        # Kill Assistants assertions

        # assists of player_2 and player_4 should be 0
        assert players_stats['player_2']['assists'] == 0
        assert players_stats['player_4']['assists'] == 0

        # player kills should be 0
        assert players_stats['player_2']['player_kills'] == 0
        assert players_stats['player_4']['player_kills'] == 0

        # their gold should be still 0
        assert players_stats['player_2']['gold'] == 0
        assert players_stats['player_4']['gold'] == 0

        # their deaths should be still 0
        assert players_stats['player_2']['deaths'] == 0
        assert players_stats['player_4']['deaths'] == 0

        # they should be still alive
        assert players_stats['player_2']['alive'] is True
        assert players_stats['player_4']['alive'] is True

    def test_killer_id_is_null(self, setup):
        """A player kills another player but killerID is null"""
        event_json = """
                {
                    "type": "PLAYER_KILL",
                    "payload":
                        {
                            "killerID": null,
                            "victimID": "player_3",
                            "goldGranted": 600,
                            "assistants": [],
                            "assistGold": 150
                        }
                    }
                """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be still 0 for all players (original value 0)
        assert players_stats['player_1']["player_kills"] == 0
        assert players_stats['player_2']["player_kills"] == 0
        assert players_stats['player_3']["player_kills"] == 0
        assert players_stats['player_4']["player_kills"] == 0
        # gold should be still 0 for all players (original value 0)
        assert players_stats['player_1']["gold"] == 0
        assert players_stats['player_2']["gold"] == 0
        assert players_stats['player_3']["gold"] == 0
        assert players_stats['player_4']["gold"] == 0

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

    def test_victim_id_is_null(self, setup):
        """A player kills another player but the victimID is null"""
        event_json = """
                        {
                            "type": "PLAYER_KILL",
                            "payload":
                                {
                                    "killerID": "player_1",
                                    "victimID": null,
                                    "goldGranted": 600,
                                    "assistants": [],
                                    "assistGold": 150
                                }
                            }
                        """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 600 (original value 0)
        assert players_stats[killer_id]["gold"] == 600
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 0 for all players, we don't know who the victim was (original value 0)
        assert players_stats['player_1']['deaths'] == 0
        assert players_stats['player_2']['deaths'] == 0
        assert players_stats['player_3']['deaths'] == 0
        assert players_stats['player_4']['deaths'] == 0
        # all players should be still alive
        assert players_stats['player_1']['alive'] is True
        assert players_stats['player_2']['alive'] is True
        assert players_stats['player_3']['alive'] is True
        assert players_stats['player_4']['alive'] is True

    def test_gold_granted_is_null(self, setup):
        """A player kills another player but the goldGranted is null"""
        event_json = """
                {
                    "type": "PLAYER_KILL",
                    "payload":
                        {
                            "killerID": "player_1",
                            "victimID": "player_3",
                            "goldGranted": null,
                            "assistants": [],
                            "assistGold": 150
                        }
                    }
                """
        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 0, since it was null in the event (original value 0)
        assert players_stats[killer_id]["gold"] == 0
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

        # Kill Assistants assertions

        # assists of player_2 and player_4 should be 0
        assert players_stats['player_2']['assists'] == 0
        assert players_stats['player_4']['assists'] == 0

        # player kills should be 0
        assert players_stats['player_2']['player_kills'] == 0
        assert players_stats['player_4']['player_kills'] == 0

        # their gold should be still 0
        assert players_stats['player_2']['gold'] == 0
        assert players_stats['player_4']['gold'] == 0

        # their deaths should be still 0
        assert players_stats['player_2']['deaths'] == 0
        assert players_stats['player_4']['deaths'] == 0

        # they should be still alive
        assert players_stats['player_2']['alive'] is True
        assert players_stats['player_4']['alive'] is True

    def test_assist_gold_is_null(self, setup):
        """A player kills another player but the assistGold is null in the event"""
        event_json = """
                {
                    "type": "PLAYER_KILL",
                    "payload":
                        {
                            "killerID": "player_1",
                            "victimID": "player_3",
                            "goldGranted": 600,
                            "assistants": [
                                "player_2"
                            ],
                            "assistGold": null
                        }
                    }
                """

        event_dict = json.loads(event_json)
        # Handle event
        self.event_handler.handle(data=event_dict, game_state=self.game_state)

        # Killer Assertions
        killer_id = event_dict["payload"]["killerID"]
        players_stats = self.game_state.players_stats

        # player_kills should be 1 (original value 0)
        assert players_stats[killer_id]["player_kills"] == 1
        # gold should be 600 (original value 0)
        assert players_stats[killer_id]["gold"] == 600
        # killer should be alive
        assert players_stats[killer_id]['alive'] is True

        # Victim Assertions
        victim_id = event_dict["payload"]["victimID"]
        # deaths should be 1 (original value 0)
        assert players_stats[victim_id]['deaths'] == 1
        # alive should be set to False
        assert players_stats[victim_id]['alive'] is False

        # Kill Assistants assertions
        assistant_id = event_dict["payload"]["assistants"][0]
        # assists should be 1
        assert players_stats[assistant_id]["assists"] == 1
        # gold should be still 0, i.e. nothing added to the previous amount
        assert players_stats[assistant_id]["gold"] == 0

