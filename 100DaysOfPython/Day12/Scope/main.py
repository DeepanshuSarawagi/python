# In this lesson we are going to learn about Scope

enemies = 1


def increase_enemies():
    global enemies  # We need to explicitly mention that we need to modify a variable which is defined outside the
                    # function
    enemies += 1
    print("enemies inside function: {}".format(enemies))


increase_enemies()
print("enemies outside function: {}".format(enemies))

player_health = 10


def drink_potion():
    potion_strength = 2  # This variable is in local scope to this function
    print(player_health)  # The variable player_health id from global/outer scope of this function


print(drink_potion())
