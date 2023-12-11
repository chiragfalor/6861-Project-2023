import json
import pandas as pd
from GameModel import GameModel

def load_games() -> list[GameModel]:
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

def load_games_with_tasks() -> list[GameModel]:
    import os
    games = load_games()
    query_games = []
    for g in games:
        code_path = g.code_file_path.split('/')[-1].split('.')[0]
        query_path = f'data/game_condition_query/{code_path}.csv'
        # if it is a valid query, load it
        if os.path.exists(query_path):
            g.queries_df = pd.read_csv(query_path, index_col=0)
            query_games.append(g)
            g.process_queries()
    return query_games
    

def load_system_prompt(file_path):
    with open(file_path) as f:
        system_prompt = f.read()
    return system_prompt


if __name__=="__main__":
    games = load_games()
    query_games = load_games_with_tasks()
