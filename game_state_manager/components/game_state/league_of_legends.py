from game_state_manager.components.game_state.base import BaseGameState
from game_state_manager.constants import Games


class LeagueOfLegendsGameState(BaseGameState):
    game_title = Games.LEAGUE_OF_LEGENDS.value

    def initialize(self, *args, **kwargs):
        """
        Initialize the game state

        :param args:
        :param kwargs:
        :return: None
        """
        for game_state_var, value in kwargs.items():
            setattr(self, game_state_var, value)
