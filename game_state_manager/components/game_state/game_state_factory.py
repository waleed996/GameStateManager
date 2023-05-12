from game_state_manager.components.game_state.league_of_legends import LeagueOfLegendsGameState
from game_state_manager.constants import Games


class GameStateFactory:
    """Factory class for all Games states"""

    def get_game_state(self, game_title):
        if game_title == Games.LEAGUE_OF_LEGENDS.value:
            return LeagueOfLegendsGameState()
        else:
            raise NotImplementedError(f"{game_title} game state not implemented!")
