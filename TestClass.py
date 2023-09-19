
class UserInfo:
    name: str
    level: int
    hp: int
    mp: int
    money: int

    def __init__(self, name, level, hp, mp, money):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.money = money


class Item:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price
