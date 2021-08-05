"""
    练习15
"""


class Pokemon:
    def __init__(self, name):
        self.name = name


class Water_Pokemon(Pokemon):
    def __init__(self, name):
        self.name = name

    def water(self):
        print('{}'.format(self.name) + '使用了技能水枪')


class Grass_Pokemon(Pokemon):
    def __init__(self, name):
        self.name = name

    def grass(self):
        print('{}'.format(self.name) + '使用了技能飞叶快刀')


class Fire_Pokemon(Pokemon):
    def __init__(self, name):
        self.name = name

    def fire(self):
        print('{}'.format(self.name) + '使用了技能喷火')


class MixPokemon(Water_Pokemon, Fire_Pokemon, Grass_Pokemon):
    def __init__(self, name):
        self.name = name


water = Water_Pokemon('杰尼龟')
water.water()
fire = Fire_Pokemon('小火龙')
fire.fire()
grass = Grass_Pokemon('妙蛙种子')
grass.grass()
mix = MixPokemon('自定义生物')
mix.water()
mix.fire()
mix.grass()
