import json
from collections import namedtuple
import DictToClass
import os


def make(data, typename):
    loadedjson = str(json.loads(data))
    print(loadedjson)
    loadedjson = loadedjson.replace(': \'', '-')
    loadedjson = loadedjson.replace(':', '-')
    print(loadedjson)
    loadedjson = loadedjson.replace('\',', '-')
    loadedjson = loadedjson.replace(',', '-')
    print(loadedjson)
    splited = loadedjson.split('\'')
    print("=============")
    for var in splited:
        print(var)
    print("=============")

    namelist = []

    for i in range(len(splited)):
        if i % 2 == 0:
            continue
        if i >= len(splited):
            continue
        print(splited[i])
        namelist.append(splited[i])

    filepath = os.getcwd()
    filepath += "\\" + typename + ".py"
    with open(filepath, 'w', encoding="utf-8") as make_file:
        make_file.write("class " + typename + ":\n\n")
        make_file.write("\t" + "def __init__(self, ")
        for i in range(len(namelist)):
            make_file.write(namelist[i])
            if i == len(namelist) - 1:
                make_file.write("):\n")
            else:
                make_file.write(", ")
        for i in range(len(namelist)):
            make_file.write("\t\t" + "self." + namelist[i] + " = " + namelist[i] + "\n")

    # loaded = json.loads(data, object_hook= customdecoder)
    # print(loaded)


def customdecoder(target):
    converted = target.__class__
    # converted = DictToClass.DictToClass(targetdict)
    return namedtuple(type(converted).__name__, target.keys())(*target.values())
