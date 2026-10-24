class Enemy:
    def __init__(self,
                 enemy_type: str,
                 deffense_points: int = 10,
                 attack_points: int = 15):
        self.enemy_type = enemy_type
        self.deffense_points = deffense_points
        self.attack_points = attack_points

    def talk(self):
        print('Enemy talks.')

    def walk(self):
        print('Enemy walks towards you.')

    def attack(self):
        print(f'Enemy attacks.')
