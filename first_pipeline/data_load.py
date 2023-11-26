
import json
from GameModel import GameModel

def load_games():
    with open('data/game_desc.json') as f:
        data = json.load(f)

    games = []
    for game in data['game_descriptions']:
        game_code_path = game['ppl_code_file_path']
        # load description
        with open(f'data/{game_code_path}') as f:
            code = f.read()
        games.append(GameModel(game['name'], game['description'], code))
        
    return games

def load_system_prompt():
    with open('system_prompt.txt') as f:
        system_prompt = f.read()
    return system_prompt
