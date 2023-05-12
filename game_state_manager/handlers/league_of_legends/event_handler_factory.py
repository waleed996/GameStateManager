"""
Handler Factory for all league of legends events
"""

from game_state_manager.constants import LeagueOfLegendsEventTypes
from game_state_manager.handlers.league_of_legends.dragon_kill_handler import DragonKillEventHandler
from game_state_manager.handlers.league_of_legends.match_end_handler import MatchEndEventHandler
from game_state_manager.handlers.league_of_legends.match_start_handler import MatchStartEventHandler
from game_state_manager.handlers.league_of_legends.minion_kill_handler import MinionKillEventHandler
from game_state_manager.handlers.league_of_legends.player_kill_handler import PlayerKillEventHandler
from game_state_manager.handlers.league_of_legends.turret_destroy_handler import TurretDestroyEventHandler
from game_state_manager.handlers.league_of_legends.unknown_event_handler import UnknownEventHandler


class LeagueOfLegendsEventHandlerFactory:
    """Factory class for League of Legends game events"""

    def get_event_handler(self, event_type):
        if event_type == LeagueOfLegendsEventTypes.MATCH_START.value:
            return MatchStartEventHandler()
        elif event_type == LeagueOfLegendsEventTypes.MATCH_END.value:
            return MatchEndEventHandler()
        elif event_type == LeagueOfLegendsEventTypes.MINION_KILL.value:
            return MinionKillEventHandler()
        elif event_type == LeagueOfLegendsEventTypes.PLAYER_KILL.value:
            return PlayerKillEventHandler()
        elif event_type == LeagueOfLegendsEventTypes.DRAGON_KILL.value:
            return DragonKillEventHandler()
        elif event_type == LeagueOfLegendsEventTypes.TURRET_DESTROY.value:
            return TurretDestroyEventHandler()
        else:
            return UnknownEventHandler()
