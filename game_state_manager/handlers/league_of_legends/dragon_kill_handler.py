from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class DragonKillEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):

        killer_player_id = data["payload"]["killerID"]

        # We cannot update the game state because we do not have any other information we can use to identify player and
        # his team
        if not killer_player_id:
            return

        # Get stats for player who killed the dragon
        player_dragon_killer = game_state.players_stats[killer_player_id]

        # If the event received is for a player that is dead, ignore the event. HOW CAN A DEAD PLAYER SLAY A DRAGON :)
        if not player_dragon_killer['alive']:
            return

        if data["payload"]["goldGranted"]:
            # Add gold to player current gold
            player_dragon_killer["gold"] += data["payload"]["goldGranted"]

        # Get team id of the player who killed the dragon
        team_id = game_state.players_team_mapping[killer_player_id]

        # Get team stats for the killer's team
        team_stats = game_state.teams_stats[team_id]
        # Increase team dragon kill count
        team_stats["dragon_kills"] += 1

