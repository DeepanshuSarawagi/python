import random
import  my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi)

random_float = random.random()
print("{:.2f}".format(random_float * random_integer))
