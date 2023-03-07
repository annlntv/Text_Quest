
from time import sleep

'''Всего 5 классов. Ведьма, гоблин, эльф, вурдалак, тролль.'''
'''Характеристики класса Ведьма

уровень здоровья: 50
класс брони: 15
сила удара: 20
оружие: магическая книга-катализатор'''

'''Характеристики класса Гоблин
Гоблины меньше людей и кажутся слабее. Вместо грубой силы они обычно устраивают засады на своих врагов, а также у них высокая вероятность удачного побега. 
Они используют отравленные стрелы и оружие.
уровень здоровья: 80
класс брони: 20
сила удара: 15
оружие: отравленные стрелы'''

'''Характеристики класса эльф
Эльфы благородны и сильны. Вместо боя они предпочтут мирные переговоры, но иногда им очень хочется чего-нибудь своровать.
уровень здоровья: 60
класс брони: 25
сила удара: 20
оружие: серебрянный меч'''



class Hero():
    # конструктор класса
    def __init__(self, name, health, armor, kind):
        self.name = name
        self.health = health
        self.armor = armor
        self.kind = kind

    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)

class Witch(Hero):

    def hello(self):
        print('->', self.name + '. Ваш выбор пал на Ведьму. С виду Ведьма похожа на человека, но, если к ней приблизиться, то можно заметить зеленоватую кожу. Она обладает навыком предсказывания будущего, и невероятно колдует с помощью своей книги.')
        self.print_info()

        # нанести удар по другому персонажу
    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой 20, используя магический катализатор\n')
        enemy.armor -= 20
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пала в этом нелегком бою, несмотря на все свои навыки предсказывания!\n')
                break
        sleep(1)


class Goblin(Hero):
    def hello(self):
        print('->', self.name + '. Ваш выбор пал на Гоблина. Гоблины меньше людей и кажутся слабее. Вместо грубой силы они обычно устраивают засады на своих врагов, а также у них высокая вероятность удачного побега. Они используют отравленные стрелы и оружие.')
        self.print_info()
        # нанести удар по другому персонажу
    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + ' устраивает засаду и атакует ' + enemy.name + ' с силой 15, используя отравленные ядом стрелы.\n')
        enemy.armor -= 15
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом нелегком бою, несмотря на всю свою хитрость!\n')
                break
        sleep(1)



class Elf(Hero):
    def hello(self):
        print('->', self.name + '. Ваш выбор пал на Эльфа. Эльфы благородны и сильны. Вместо боя они предпочтут мирные переговоры, но иногда им очень хочется чего-нибудь своровать.')
        self.print_info()

        # нанести удар по другому персонажу
    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + ' изящно атакует ' + enemy.name + ' с силой 25, используя серебряный меч\n')
        enemy.armor -= 25
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, ' пал в этом нелегком бою!\n')
                break
        sleep(1)


class Troll(Hero):
    def hello(self):
        print('->', self.name + '. Ваш выбор пал на Тролля.')
        self.print_info()
        # нанести удар по другому персонажу

    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + 'агрессивно атакует ' + enemy.name + 'с силой 20, используя огромную дубину с шипами.\n')
        enemy.armor -= 20
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом нелегком бою!\n')
                break
        sleep(1)


class Vamp(Hero):
    def hello(self):
        print('->', self.name + '. Ваш выбор пал на Вурдалака.')
        self.print_info()
        # нанести удар по другому персонажу
    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой 15, используя свои заточенные клыки и когти.\n')
        enemy.armor -= 15
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'умер в этом нелегком бою от последнего удара своего врага!\n')
                break
        sleep(1)

class Monster(Hero):

    def strike(self, enemy):
        sleep(1)
        print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой 10, используя смертоносные навыки.\n')
        enemy.armor -= 10
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        sleep(1)

        print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

    # вступить в поединок
    def fight(self, enemy):
        h = enemy.health
        a = enemy.armor
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                sleep(1)
                return 'победа'
            sleep(1)

            enemy.strike(self)
            if self.health <= 0:
                sleep(1)
                enemy.health = h
                enemy.armor = a
                return 'поражение'
        sleep(1)