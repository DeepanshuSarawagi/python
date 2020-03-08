from player import Player
from enemy import Enemy, Troll

deep = Player("Deepanshu")
print(deep.name)

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll()
print(ugly_troll)
