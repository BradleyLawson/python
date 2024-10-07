class Attack:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

  def __str__(self):
    return f'{self.name} does {self.damage} damage.'