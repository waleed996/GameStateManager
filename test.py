import os
import json

data_path = os.getcwd() + '/league_of_legends_data/data/'

file_event_names = os.listdir(data_path)
file_event_names.sort()
match_start = []
match_end = []
unknown_events = []
decode_errors = []
for file_name in file_event_names:
    with open(data_path + file_name, 'r') as event_json_file:
        try:
            # Try to load the json event data
            event_data = json.load(event_json_file)

            if event_data["type"] == "MATCH_START":
                match_start.append(file_name)
            elif event_data["type"] == "MATCH_END":
                match_end.append(file_name)
            elif event_data["type"] == "UNKNOWN":
                unknown_events.append(file_name)

        except json.JSONDecodeError as err:  # Handle json decode error
            decode_errors.append(file_name)

        except Exception as err:  # Catch any other unhandled errors as a fallback
            print(f"Unhandled Error occurred while parsing event {file_name} , error: {str(err)}")
            continue


print(match_start)
print("\n\n")
print(match_end)
print("\n\n")
print(unknown_events)
print("\n\n")
print(decode_errors)

