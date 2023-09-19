import json
import os


def make(targetclass):
    filepath = os.getcwd()
    filepath += "\\" + type(targetclass).__name__ + ".json"
    with open(filepath, 'w', encoding='utf-8') as make_file:
        json.dump(targetclass.__dict__, make_file, indent="\t")


def get(targetclass):
    return json.dumps(targetclass.__dict__, indent="\t")