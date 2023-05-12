from game_state_manager.handlers.base import LeagueOfLegendsEventHandler


class UnknownEventHandler(LeagueOfLegendsEventHandler):

    def handle(self, data, game_state):
        # Log the unknown event for debugging purposes
        print(f"League Of Legends Unknown event received: {str(data)}")
