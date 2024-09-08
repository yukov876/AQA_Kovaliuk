from typing import override

from lesson_16.homework_16_2.figure import Figure


class Square(Figure):
    __square_side: int

    def __init__(self, square_side: int):
        self.__square_side = square_side

    @override
    def calculate_perimetr(self) -> int:
        return self.__square_side * 4

    @override
    def calculate_square(self) -> int:
        return self.__square_side ** 2
