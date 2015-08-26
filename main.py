import sys
import json

def create_new_json():
    data = {
            'wins': 0,
            'loses': 0,
            'winrate': 0,
            'goals': 0,
            'goalsOnYou': 0,
            'wins1v1': 0,
            'loses1v1': 0,
            'winrate1v1': 0,
            'wins2v2': 0,
            'loses2v2': 0,
            'winrate': 0,
            'wins3v3': 0,
            'loses3v3': 0,
            'winrate3v3': 0
    }
    encoded_json = (json.dumps(data))

    with open('data.json', 'w') as data_file:
        data_file.write(encoded_json)
