class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {self._hit_points} points left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} has lost a life")
            else:
                print(f"{self._name} is dead.")
                self._alive = False

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit Points: {self._hit_points}"


class Troll(Enemy):
    """Creating sub-class Troll and its properties will be inherited from super class Enemy"""
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me ugly {self._name}. {self._name} stomps you.")


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print(f"**** {self._name} dodges ****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):

    def __init__(self, name, hit_points=140):
        super().__init__(name=name)
        self._hit_points = hit_points

    def take_damage(self, damage):
        damage = damage // 4
        damage = int(damage)
        super().take_damage(damage=damage)
