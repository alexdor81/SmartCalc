import string
import math


class ModelCalc:

    def __init__(self):
        self.numbers = []
        self.operators = []

    def calculate(self, str_input, x):
        self.numbers.clear()
        self.operators.clear()
        result = 0.0
        number = ""
        str_output = self.validation(str_input)
        while str_output:
            if str_output[0] in string.digits + ".e":
                number += str_output[0]
                if str_output[0] in "e" and str_output[1] in "+-":
                    number += str_output[1]
                    str_output = str_output[1:]
                elif len(str_output) == 1 or str_output[1] not in string.digits + ".e":
                    self.numbers.append(float(number))
                    number = ""
            elif str_output[0] in "x":
                self.numbers.append(x)
            else:
                self.__read_symbol(str_output[0])
            str_output = str_output[1:]
        while self.operators:
            self.__calculations()
        if self.numbers:
            result = self.numbers.pop()
        return result

    def validation(self, str_input):
        str_output = ""
        i = 0
        while i < len(str_input):
            if str_input[i] in "+-" and (i == 0 or str_input[i - 1] in "+-*/("):
                if str_input[i] == "-":
                    str_output += "u"
                i += 1
            if str_input[i] in "acstlm":
                if str_input[i] in "a" or str_input[i + 1] in "q":
                    str_output += chr(ord(str_input[i + 1]) - 32)
                    i += 4
                elif str_input[i] in "l" and str_input[i + 1] in "n":
                    str_output += "L"
                    i += 2
                else:
                    str_output += str_input[i]
                    i += 3
            str_output += str_input[i]
            i += 1
        return str_output

    def __read_symbol(self, symbol):
        if symbol in "(" or not self.operators:
            self.operators.append(symbol)
        elif symbol in ")":
            while self.operators[-1] not in "(":
                self.__calculations()
            self.operators.pop()
        else:
            while self.operators and self.__priority(
                self.operators[-1]
            ) >= self.__priority(symbol):
                self.__calculations()
            self.operators.append(symbol)

    def __calculations(self):
        result = 0.0
        func = self.operators.pop()
        if func in "usScCtTlLQ":
            a = self.numbers.pop()
            match func:
                case "s":
                    result = math.sin(a)
                case "c":
                    result = math.cos(a)
                case "t":
                    result = math.tan(a)
                case "S":
                    result = math.asin(a)
                case "C":
                    result = math.acos(a)
                case "T":
                    result = math.atan(a)
                case "L":
                    result = math.log(a)
                case "l":
                    result = math.log10(a)
                case "Q":
                    result = math.sqrt(a)
                case "u":
                    result = -1 * a
        else:
            a = self.numbers.pop()
            b = self.numbers.pop()
            match func:
                case "+":
                    result = b + a
                case "-":
                    result = b - a
                case "*":
                    result = b * a
                case "/":
                    result = b / a
                case "^":
                    result = b**a
                case "m":
                    result = math.fmod(b, a)
        self.numbers.append(result)

    def __priority(self, symbol):
        result = 0
        if symbol in "+-":
            result = 1
        elif symbol in "*/m":
            result = 2
        elif symbol in "u":
            result = 3
        elif symbol in "^":
            result = 4
        elif symbol in "sScCtTlLQ":
            result = 5
        return result
