class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {self.hit_points} points left")
        else:
            self.lives -= 1

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit Points: {self.hit_points}"


class Troll(Enemy):
    """Creating sub-class Troll and its properties will be inherited from super class Enemy"""
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)
