import json
from collections import namedtuple
import DictToClass


def make(data):

    loaded = json.loads(data, object_hook= customdecoder)
    print(loaded)


def customdecoder(targetdict):

    converted = DictToClass.DictToClass(targetdict)
    return namedtuple(type(converted).__name__, targetdict.keys())(*targetdict.values())
