from enemy import *

class Ogre(Enemy):

    def __init__(self, deffense_points = 20, attack_points = 30):
        super().__init__(enemy_type = 'Ogre',
                         deffense_points = deffense_points,
                         attack_points = attack_points)
        
    def talk(self):
        print('Ogre slams hands all around.')

    def destroy(self):
        print('Ogre destroys stuff.')
