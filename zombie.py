from enemy import *

class Zombie(Enemy):
    def __init__(self, deffense_points = 10, attack_points = 15):
        super().__init__(enemy_type = 'Zombie',
                         deffense_points = deffense_points,
                         attack_points = attack_points)

    def talk(self):
        print('Grrrr')

    def spread_disease(self):
        print('Zombie spreads disease.')
