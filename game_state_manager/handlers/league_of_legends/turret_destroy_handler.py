import copy

from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class TurretDestroyEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):

        killer_team_id = data["payload"]["killerTeamID"]
        killer_player_id = data["payload"]["killerID"]

        # if no killer team id in the event but killer player id is found, Set the killer_team_id from game_state
        if not killer_team_id and killer_player_id:
            killer_team_id = game_state.players_team_mapping[killer_player_id]

        # If the killer player is dead, ignore the event
        if killer_player_id and not game_state.players_stats[killer_player_id]['alive']:
            return

        if killer_team_id:
            # Get stats for the team who destroyed the turret
            team_stats = game_state.teams_stats[killer_team_id]
            # Increase teams tower kill count
            team_stats["turrets_destroyed"] += 1

            # Grant team gold to all team members, except the player who destroyed the turret, he will get player gold
            team_players_ids = copy.deepcopy(game_state.team_players_list[killer_team_id])
            # Remove the player killerID, if we have killerID in the event
            if killer_player_id:
                team_players_ids.remove(killer_player_id)

            # Add team gold for each team player
            for player_id in team_players_ids:
                game_state.players_stats[player_id]["gold"] += data["payload"]["teamGoldGranted"]

        # Add gold for the killer player if tower is destroyed by player
        if killer_player_id:
            game_state.players_stats[killer_player_id]["gold"] += data["payload"]["playerGoldGranted"]
