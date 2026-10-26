from enemy import *

zombie = Enemy('Zombie')

print(f'{zombie.get_enemy_type()} has {zombie.deffense_points} defense points, '
    f'and {zombie.attack_points} attack points.')

zombie.talk()
