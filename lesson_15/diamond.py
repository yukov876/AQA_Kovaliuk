class Diamond:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a
        self.corner_b = int((360 - (self.corner_a * 2))/2)

    def __setattr__(self, key, value):
        if key == 'side_a' and value <= 0:
            raise ValueError("Сторона а повинна бути більше 0")
        if key == 'corner_a' and key == 'corner_b' and diamond.corner_a+diamond.corner_b != 180:
            raise ValueError("Сума кутів а та b має дорівнювати 180")
        super().__setattr__(key, value)


diamond = Diamond(10,70)
