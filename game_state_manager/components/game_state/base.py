"""
Base game state for all games
"""

import inspect
import json

from abc import ABC, abstractmethod


class BaseGameState(ABC):
    """Base class for all games states representation"""

    @abstractmethod
    def initialize(self, *args, **kwargs):
        """
        Abstract method for game state initialization, inherit this class and implement this method for all the
        different game states

        :return: None
        """
        raise NotImplementedError()

    def display_game_state(self):
        """
        Prints the current game state
        :return: None
        """

        print(f"Game State Representation for Game State type: {self.__class__.__name__}")
        for attr_name, attr_value in self.__dict__.items():
            if not attr_name.startswith("__") and not inspect.isroutine(attr_value):
                print(f"{attr_name} : {json.dumps(attr_value, indent=4)}")


class BaseGameStateManager(ABC):
    """Base class for all the games' game state manager subclasses"""

    @abstractmethod
    def consume(self, data_path):
        """
        Consume game event data
        :param data_path: data directory containing game events
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def _parse_game_event(self, event_obj):
        """
        Abstract method for reading game events from a source, inherit this class and implement this method for all the
        different games' state managers
        :param event_obj: Event object, can be a dict, file etc
        :return: Parsed Object
        """
        raise NotImplementedError()

    @abstractmethod
    def _process_game_event(self, event_data):
        """
        Abstract method for processing a game event, inherit this class and implement this method for all the different
        games' state managers
        :param event_data: event data to be processed
        :return: None
        """
        raise NotImplementedError()

