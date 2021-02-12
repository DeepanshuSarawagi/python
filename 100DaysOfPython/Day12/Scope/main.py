# In this lesson we are going to learn about Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print("enemies inside function: {}".format(enemies))


increase_enemies()
print("enemies outside function: {}".format(enemies))
