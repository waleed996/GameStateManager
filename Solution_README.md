# Author
waleedabbasi996@gmail.com

# Note
Because of time constraints I was not able to do string manipulation for unparsable/incomplete events.
At the moment they are just logged to the terminal.

# Design Overview

Overall thought process behind the design is to keep it as generic, scalable and
extensible as possible. With minor changes it can easily be used to manage state
of multiple games. 

## League Of Legends Game State Representation
Following are the state maps that represent one league of legends match. All these
maps are dynamically set to the Game State object. This provides flexibility in the design to accomodate
more game state information if needed in the future, making the solution scalable. This approach
also has the added advantage of reducing the time complexity to O(1) in most cases.

```
game_info
{
    'title': data['payload']['fixture']['title'],
    'match_id': data['matchID'],
    'start_time': data['payload']['fixture']['startTime'],
    'series_current': data['payload']['fixture']['seriesCurrent'],
    'series_max': data['payload']['fixture']['seriesMax'],
    'series_type': data['payload']['fixture']['seriesType'],
    'match_state': 'IN_PROGRESS' || 'ENDED' etc,
    'end_time': None,
    'winning_team_id': winner_team_id
}

players_team_mapping
{
    "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed": "riot:lol:team:101383793574360315",
    ... n
}

team_players_list
{
    "riot:lol:team:101383793574360315": [
        "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed",
        "riot:lol:player:f114d45a-be6d-38a1-b163-525423d232ss",
        ... n
    ],
    "riot:lol:team:101383793574360315": [... n],
    ... n
}

teams_stats
{
    "riot:lol:team:101383793574360315": {
        'dragon_kills': 0,
        'turrets_destroyed': 0
    }, ... n
}

players_stats
{
    "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed": {
        "playerID": "riot:lol:player:f114d45a-be6d-38a1-b163-525423dee8ed",
        "gold": 0,
        "name": "",
        'minion_kills': 0,
        'player_kills': 0,
        'deaths': 0,
        'assists': 0,
        'alive': True
    }, ... n
}
```

## Game State
A dynamic representation of the state of a game. Using abstract base classes and methods, the impementation
allows for better code management and encapsulation.

The BaseGameState can be inherited for new game states. 

## Game State Factory
A factory class to return game state instances for more than one game while conforming to
the same interface provided by `BaseGameState` class.

Allows to conveniently get new game states whenever needed.

## Game State Manager
This is the controller/manager of a game's state.

The implementation allows multiple game state managers for each game by 
extending the `BaseGameStateManager` class while conforming to a single interface.

## Event Handlers
Each event type has a separate event handler class which extends the `BaseGameEventHandler`.

The factory class returns an event handler by type wherever it is needed.


## How to Run the Application
The application is a simple python script based application.

Follow these steps to run it:
1. Create a virtual environment using the command ```python -m venv venv```
2. Activate the virtual environment using the command ```source venv/bin/activate``` (venv is the name of the virtual environment)
3. Install the `requirements.txt` file after activating the virtual environment and running the command
```pip install -r requirements.txt```. This will install the dependencies from the requirements file.
4. Finally, just run the `main.py` file by using the command `python main.py`

In case there are any problems, please don't hesitate to contact me via email.

