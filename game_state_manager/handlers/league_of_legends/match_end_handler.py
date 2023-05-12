import datetime

from game_state_manager.constants import LeagueOfLegendsSeriesMatchStates, LeagueOfLegendsDateTimeFormats
from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class MatchEndEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):

        # Get game info
        game_info = game_state.game_info

        # Update match state
        game_info["match_state"] = LeagueOfLegendsSeriesMatchStates.ENDED.value

        # Update match end time
        end_time_utc = datetime.datetime.now(datetime.timezone.utc).strftime(
            LeagueOfLegendsDateTimeFormats.ISO_FORMAT.value)
        game_info["end_time"] = end_time_utc

        # Update winning team id
        game_state.game_info['winning_team_id'] = data["payload"]["winningTeamID"]

