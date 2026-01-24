class Rhombus:
    def __init__(self, side, angle_a, angle_b):
        self.side = int(side)
        self.angle_a = int(angle_a)
        self.angle_b = int(angle_b)

    def __setattr__(self, name, value):

        super().__setattr__(name, value)

        if name == 'side' and value <= 0:
            raise ValueError(f"Side must be > 0. You set side {value}")
        elif hasattr(self, 'angle_a') and hasattr(self, 'angle_b'):
            if self.angle_a + self.angle_b != 180:
                raise ValueError("Sum of 'angle_a' and 'angle_b' must be equal to 180")

    def __str__(self):
        return f"""Your rhombus has side {self.side}
And two angles. 'angle_a' is {self.angle_a}, 'angle_b' is {self.angle_b}
Perimeter of the rhombus is {self.side*4} """

rombus_correct = Rhombus("5", angle_a="70", angle_b=110)
print(rombus_correct)

# rombus_with_incorrect_side = Rhombus(0, 150, 20)
# print(rombus_with_incorrect_side)

rombus_with_incorrect_angles = Rhombus(6, 150, "500")
print(rombus_with_incorrect_angles)

# rombus_with_all_incorrect = Rhombus(-4, 150, "200")
# print(rombus_with_all_incorrect)


