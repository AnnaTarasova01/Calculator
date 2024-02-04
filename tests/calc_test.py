from calc import Calculator
import pytest


class TestCalc:
    def test_multiply_correctly(self):
        """проверка корректного умножения"""

        self.calc = Calculator
        assert self.calc.multiply(self, 2, 5) == 10

    def test_division_correctly(self):
        """Проверка корректного деления"""

        self.calc = Calculator
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_correctly(self):
        """Проверка корректного вычитания"""

        self.calc = Calculator
        assert self.calc.subtraction(self, 24, 26) == -2

    def test_adding_correctly(self):
        """Проверка корректного сложения"""

        self.calc = Calculator
        assert self.calc.adding(self, -5, 5) == 0