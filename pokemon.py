class Pokemon:
    def __init__(self, name: str, attack_points, defense_points, health_points, moves):
        self.name = name
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.health_points = health_points
        self.moves = moves
    
    def attack(self, other):
        print(f'{self.name} attacked {other.name}')
        other.health_points -= self.attack_points

    def __repr__(self) -> str:
        return f'This is a {self.name}, and it has {self.attack_points} attack point'

    def __gt__(self, other):
        return self.health_points > other.health_points

print(__name__)
if __name__ == "__main__":
    pikachu = Pokemon(name='Pikachu', attack_points=25, defense_points=40, health_points=100, moves=[])
    print(pikachu)