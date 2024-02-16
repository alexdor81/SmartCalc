"""Module for testing the calculation model"""
import math
import unittest
from model.model_calc import ModelCalc

str_input = ["5e+2+3+1",
             "2^2^3",
             "+2*(4.1234567/4+(-24.1234567)/4)",
             "36.11+(-285.3)+2*5/736.2-(-144)*42-74/4.3+(-0.123)+12*(0.5+4)/(-3)",
             "2^sin(x)-log(20)",
             "cos(-sin(3^2)*4)+1",
             "-2-(-16)-7-sqrt(256)",
             "sin(tan(x))"]

model = ModelCalc()


class TestCalculator(unittest.TestCase):
    def test_0(self):
        res = model.calculate(str_input[0], 0)
        sample = eval(str_input[0])
        self.assertEqual(res, sample)

    def test_1(self):
        res = model.calculate(str_input[1], 0)
        sample = (2 ** 2) ** 3
        self.assertEqual(res, sample)

    def test_2(self):
        res = model.calculate(str_input[2], 0)
        sample = eval(str_input[2])
        self.assertEqual(res, sample)

    def test_3(self):
        res = model.calculate(str_input[3], 0)
        sample = eval(str_input[3])
        self.assertEqual(res, sample)

    def test_4(self):
        res = model.calculate(str_input[4], 2)
        sample = 2 ** math.sin(2) - math.log10(20)
        self.assertEqual(res, sample)

    def test_5(self):
        res = model.calculate(str_input[5], 0)
        sample = math.cos(-math.sin(3 ** 2) * 4) + 1
        self.assertEqual(res, sample)

    def test_6(self):
        res = model.calculate(str_input[6], 0)
        sample = -2 - (-16) - 7 - math.sqrt(256)
        self.assertEqual(res, sample)

    def test_7(self):
        res = model.calculate(str_input[7], 3)
        sample = math.sin(math.tan(3))
        self.assertEqual(res, sample)


if __name__ == "__main__":
    unittest.main()
