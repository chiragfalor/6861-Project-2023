
import json
import pandas as pd
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
        games.append(GameModel(game['name'], game['description'], code, game_code_path))
        
    return games

def load_system_prompt(file_path):
    with open(file_path) as f:
        system_prompt = f.read()
    return system_prompt


