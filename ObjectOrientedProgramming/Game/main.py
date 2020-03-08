from player import Player
from enemy import Enemy, Troll, Vampyre

deep = Player("Deepanshu")
print(deep.name)

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll("Ugly Troll")
print(ugly_troll)

another_troll = Troll("Ug")
print(f"Another Troll- {another_troll}")

brother = Troll("Urg")
print(brother)
brother.grunt()

vampire = Vampyre("Deadly Vampire")
print(vampire)
vampire.take_damage(3)
print(vampire)

another_troll.take_damage(12)
print(another_troll)

print("*" * 50)

while vampire._alive:
    vampire.take_damage(1)
