from player import Player

deep = Player("Deepanshu")
print(deep.name)
print(deep._score)
print(deep.lives)

deep.level = 2
print(deep)

deep.level = 4
print(deep)

deep.level = 3
print(deep)

deep.score = 1000
print(deep)
