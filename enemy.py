class Enemy:
    enemy_type: str
    attack: int = 10
    defense: int = 15
    
    def talk(self):
        print('Enemy talks.')

    def walk(self):
        print('Enemy walks towards you.')

    def attack(self):
        print(f'Enemy attacks.')
