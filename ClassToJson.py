import json
import os
import DictToClass


def make(target):

    filepath = os.getcwd()
    filepath += "\\" + type(target[0]).__name__ + "Data" + ".json"

    dictlist = []
    for data in target:
        dictlist.append(data.__dict__)

    with open(filepath, 'w', encoding='utf-8') as make_file:
        json.dump(dictlist, make_file, indent="\t")


def get(targetclass):
    return json.dumps(targetclass.__dict__, indent="\t")