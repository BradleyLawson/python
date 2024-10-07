from game.characters.sprite import Sprite
from game.combat.attack import Attack
from game.sound.battle_effects import playBattleSounds
from game.sound.music import playMusic


playMusic()
sprite = Sprite('spritty the sprite', 100, 10, 5)
print(sprite)


playBattleSounds()
attack = Attack('spritty the sprite', int(input('Enter damage: ')))

sprite.health = sprite.health - attack.damage

if sprite.health > 0:
  print(sprite)
else:
  print(f'{sprite.name} has died.')