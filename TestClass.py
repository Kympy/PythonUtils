class UserInfo:
    name = ""
    level = 0
    hp = 100
    mp = 100
    money = 0
    def __init__(self, name, level, hp, mp, money):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.money = money

class Item:
    name = ""
    price = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
