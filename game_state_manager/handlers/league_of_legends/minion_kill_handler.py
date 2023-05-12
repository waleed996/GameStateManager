from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class MinionKillEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):
        """Handles the MINION_KILL event, updates player stats"""

        if data["payload"]["playerID"]:
            # Get player's stats dict
            player_stats_dict = game_state.players_stats[data["payload"]["playerID"]]

            # If player is dead ignore this event, A dead player cannot kill a minion
            if not player_stats_dict["alive"]:
                return

            # Update minion kill count
            player_stats_dict["minion_kills"] += 1

            # Add gold to player gold
            player_stats_dict["gold"] += data["payload"]["goldGranted"]

