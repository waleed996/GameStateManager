import os
import json

from game_state_manager.components.game_state.base import BaseGameStateManager
from game_state_manager.constants import LeagueOfLegendsEventTypes
from game_state_manager.handlers.league_of_legends.event_handler_factory import LeagueOfLegendsEventHandlerFactory


class LeagueOfLegendsGameStateManager(BaseGameStateManager):
    def __init__(self, league_of_legends_game_state):
        self.game_state = league_of_legends_game_state
        self.lol_event_handler_factory = LeagueOfLegendsEventHandlerFactory()

    def consume(self, data_path):
        """
        Consume events from the data path
        :param data_path: data directory containing game events
        :return: None
        """
        file_event_names = os.listdir(data_path)
        file_event_names.sort()
        for file_name in file_event_names:
            with open(data_path + file_name, 'r') as event_json_file:
                try:
                    # Parse event
                    parsed_event = self._parse_game_event(event_obj=event_json_file)

                    # Process event
                    self._process_game_event(event_data=parsed_event)

                    print(f"{file_name} event processing finished \n\n")
                except Exception as err:
                    print(f"Error while consuming event message : {file_name}")

    def _parse_game_event(self, event_obj):
        """
        Parse event object
        :param event_obj: Event File object
        :return: dict if json can be converted else str
        """

        try:
            # Try to load the json event data
            event_data = json.load(event_obj)
            print(json.dumps(event_data, indent=4))
            return event_data
        except json.JSONDecodeError as err:
            print(f"Error while decoding file {str(event_obj)} , error: {str(err)}")
            # load file content as string, to try to process as string
            return event_obj.read()
        except Exception as err:
            print(f"Unhandled Error occurred while parsing event {str(event_obj)} , error: {str(err)}")
            raise err

    def _process_game_event(self, event_data):
        """
        Process a game event
        :param event_data: Event data to be processed
        :return: None
        """

        try:
            # Process the event data
            if isinstance(event_data, dict):
                event_type = event_data["type"]
                event_handler = self.lol_event_handler_factory.get_event_handler(event_type=event_type)
                event_handler.handle(data=event_data, game_state=self.game_state)

            else:
                # If 'type' is found in malformed json event try to process it, otherwise ignore/skip it
                if 'type' in event_data:
                    # Search for League of legends event types in event_data string
                    for event_type in LeagueOfLegendsEventTypes.as_list():
                        if event_type in event_data:
                            break
                else:
                    print(f"Skipping malformed event: -- {str(event_data)} --, event type not found.")

        except Exception as err:
            print(f"Could not process game event \n {str(event_data)} \n , error: {str(err)}")

