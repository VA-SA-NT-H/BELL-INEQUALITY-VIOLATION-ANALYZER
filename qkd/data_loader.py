import json

def get_sample_data(filepath='data/sample_run.json'):
    with open(filepath, 'r') as f:
        return json.load(f)