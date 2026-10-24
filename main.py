from enemy import *

zombie = Enemy()

zombie.enemy_type = 'Zombie'

print(f'{zombie.enemy_type} has {zombie.defense} defense points, and {zombie.attack} attack points.')

zombie.talk()
