
class DictToClass(object):

    def __init__(self, targetDict):

        for key in targetDict:
            setattr(self, key, targetDict[key])
