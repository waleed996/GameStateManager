from enum import Enum


class GameStateManagerEnum(Enum):
    """
    Base Enum class for all enums in Game State Manager constants.
    Methods can be added to manipulate/transform enum as needed.
    """

    @classmethod
    def as_list(cls):
        return list(map(lambda c: c.value, cls))


class Games(GameStateManagerEnum):
    LEAGUE_OF_LEGENDS = "LEAGUE_OF_LEGENDS"


class LeagueOfLegendsEventTypes(GameStateManagerEnum):
    MATCH_START = "MATCH_START"
    MATCH_END = "MATCH_END"
    MINION_KILL = "MINION_KILL"
    PLAYER_KILL = "PLAYER_KILL"
    DRAGON_KILL = "DRAGON_KILL"
    TURRET_DESTROY = "TURRET_DESTROY"
    UNKNOWN = "UNKNOWN"


class LeagueOfLegendsSeriesMatchStates(GameStateManagerEnum):
    IN_PROGRESS = "IN_PROGRESS"
    ENDED = "ENDED"


class LeagueOfLegendsDateTimeFormats(GameStateManagerEnum):
    ISO_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
