class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # Method to take damage
    def take_damage(self, damage):
        self.health -= damage

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"{arthur.name}'s HP: {arthur.health}")
print(f"{morgana.name}'s HP: {morgana.health}")
