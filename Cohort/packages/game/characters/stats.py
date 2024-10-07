class Stats:
  def __init__(self, name, health, attack, defense):
    self.name = name
    self.health = health
    self.attack = attack
    self.defense = defense

  def __str__(self):
    return f'{self.name} has {self.health} health, {self.attack} attack, and {self.defense} defense.'