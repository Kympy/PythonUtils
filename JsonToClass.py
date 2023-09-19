import json


def make(data):
    loaded = json.loads(data)
    print(type(loaded).__name__)
