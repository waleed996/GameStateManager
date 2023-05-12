"""
Base handler for all games
"""

from abc import abstractmethod


class BaseGameEventHandler:
    """Base class for all games event handlers"""

    @abstractmethod
    def handle(self, data, game_state):
        raise NotImplementedError()


class LeagueOfLegendsEventHandler:
    """Base event handler for all games"""

    @abstractmethod
    def handle(self, data, game_state):
        raise NotImplementedError()

