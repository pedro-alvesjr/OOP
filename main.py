from enemy import *
from zombie import *
from ogre import *

zombie = Zombie()
ogre = Ogre()

print(f'{zombie.get_enemy_type()} has {zombie.deffense_points} defense points, '
    f'and {zombie.attack_points} attack points.')
print(f'{ogre.get_enemy_type()} has {ogre.deffense_points} defense points, '
    f'and {ogre.attack_points} attack points.')

zombie.talk()
ogre.destroy()
