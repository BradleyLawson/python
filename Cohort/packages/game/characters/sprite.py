from game.characters.stats import Stats

class Sprite(Stats):
  def __init__(self, name, health, attack, defense):
    super().__init__(name, health, attack, defense)

  def __str__(self):
    return f'{self.name} has {self.health} health, {self.attack} attack, and {self.defense} defense.'