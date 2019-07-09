class Hero:
    name: ''
    hp: 0
    mana: 0
    major: ''


    def __init__(self, name, hp, mana, major):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.major = major

    def say_hello(self):
        print(self.name, "->",self.hp, "->", self.mana, "->", self.major)