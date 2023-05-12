from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class PlayerKillEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):

        if data["payload"]["killerID"]:
            # Get the killer player information
            player_killer = game_state.players_stats[data["payload"]["killerID"]]

            # A dead player cannot kill another player, ignore the event in this case
            if not player_killer['alive']:
                return

            # Increase player 'player_kills' count
            player_killer["player_kills"] += 1

            if data["payload"]["goldGranted"]:
                # Add gold to killer player gold
                player_killer["gold"] += data["payload"]["goldGranted"]

        if data["payload"]["victimID"]:
            # Increase death count of the victim
            player_victim = game_state.players_stats[data["payload"]["victimID"]]

            # A dead player cannot die again
            if not player_victim['alive']:
                return

            player_victim["deaths"] += 1
            # Set alive to False
            player_victim["alive"] = False

        if data["payload"]["assistants"]:
            # Increase assist count of assistants and add gold for the assist
            for assistant_player_id in data["payload"]["assistants"]:
                player_assistant = game_state.players_stats[assistant_player_id]

                # Increase assist count
                player_assistant["assists"] += 1

                # Add assist gold
                if data["payload"]["assistGold"]:
                    player_assistant["gold"] += data["payload"]["assistGold"]

