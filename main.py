from enemy import *

zombie = Enemy('Zombie')

print(f'{zombie.enemy_type} has {zombie.deffense_points} defense points, '
    f'and {zombie.attack_points} attack points.')

zombie.talk()
