"""Module for testing the calculation model"""
import math
import unittest
from model.model_calc import ModelCalc

str_input = ["5+2+3+1",
             "2^2^3",
             "+2*(4.1234567/4+(-24.1234567)/4)",
             "36.11+-285.3+2*5/736.2--144*42-74/4.3+-0.123+12*(0.5+4)/-3",
             "2^sin(x)-log(20)",
             "cos(-sin(3^2)*4)+1",
             "-2-(-16)-7-sqrt(256)+ln(3)",
             "sin(tan(x))",
             "asin(0)+acos(0)",
             "8mod5+atan(0.1)*1.5-10.567*-7",
             "tan(asin(-0.68))",
             "2+3.56+-1*(1.4289056/2.5+-0.5434890322e+5/36)",
             "2^(4+0.5)",
             "7mod2"]


class TestCalculator(unittest.TestCase):
    def test_0(self):
        res = ModelCalc.calculate(str_input[0], 0)
        sample = eval(str_input[0])
        self.assertEqual(res, sample)

    def test_1(self):
        res = ModelCalc.calculate(str_input[1], 0)
        sample = (2 ** 2) ** 3
        self.assertEqual(res, sample)

    def test_2(self):
        res = ModelCalc.calculate(str_input[2], 0)
        sample = eval(str_input[2])
        self.assertEqual(res, sample)

    def test_3(self):
        res = ModelCalc.calculate(str_input[3], 0)
        sample = eval(str_input[3])
        self.assertEqual(res, sample)

    def test_4(self):
        res = ModelCalc.calculate(str_input[4], 2)
        sample = 2 ** math.sin(2) - math.log10(20)
        self.assertEqual(res, sample)

    def test_5(self):
        res = ModelCalc.calculate(str_input[5], 0)
        sample = math.cos(-math.sin(3 ** 2) * 4) + 1
        self.assertEqual(res, sample)

    def test_6(self):
        res = ModelCalc.calculate(str_input[6], 0)
        sample = -2 - (-16) - 7 - math.sqrt(256) + math.log(3)
        self.assertEqual(res, sample)

    def test_7(self):
        res = ModelCalc.calculate(str_input[7], 3)
        sample = math.sin(math.tan(3))
        self.assertEqual(res, sample)

    def test_8(self):
        res = ModelCalc.calculate(str_input[8], 0)
        sample = math.asin(0) + math.acos(0)
        self.assertEqual(res, sample)

    def test_9(self):
        res = ModelCalc.calculate(str_input[9], 0)
        sample = math.fmod(8, 5) + math.atan(0.1) * 1.5 - 10.567 * -7.0
        self.assertEqual(res, sample)

    def test_10(self):
        res = ModelCalc.calculate(str_input[10], 0)
        sample = math.tan(math.asin(-0.68))
        self.assertEqual(res, sample)

    def test_11(self):
        res = ModelCalc.calculate(str_input[11], 0)
        sample = eval(str_input[11])
        self.assertEqual(res, sample)

    def test_12(self):
        res = ModelCalc.calculate(str_input[12], 0)
        sample = 2 ** (4 + 0.5)
        self.assertEqual(res, sample)

    def test_13(self):
        res = ModelCalc.calculate(str_input[13], 0)
        sample = math.fmod(7, 2)
        self.assertEqual(res, sample)


if __name__ == "__main__":
    unittest.main()
