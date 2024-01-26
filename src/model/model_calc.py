import string
import math


class ModelCalc:

    def calculate(self, str_input, x):
        self.numbers = []
        self.operators = []
        result = 0.0
        number = ""
        str_output = self.__validation(str_input)
        for i in range(len(str_output)):
            if str_output[i] in string.digits + ".e":
                number = number + str_output[i]
                if str_output[i] == 'e' and str_output[i + 1] in "+-":
                    number = number + str_output[i + 1]
                    str_output = str_output[:i + 1] + str_output[i + 2:]
                elif i == len(str_output) - 1 or str_input[i + 1] not in string.digits + ".e":
                    self.numbers.append(float(number))
                    number = ""
            elif str_output[i] in 'x':
                self.numbers.append(x)
            else:
                self.__read_symbol(str_output[i])
        while len(self.operators):
            self.__calculations()
        if len(self.numbers):
            result = self.numbers.pop()
        return result

    def __validation(self, str_input):
        str_output = ""
        i = 0
        while i < len(str_input):
            if (not i or str_input[i - 1] in "+-*/(") and str_input[i] in "+-":
                if str_input[i] == '-':
                    str_output = str_output + 'u'
                i = i + 1
            if str_input[i] in "acstlm":
                if str_input[i] in 'a' or str_input[i + 1] in 'q':
                    str_output = str_output + chr(ord(str_input[i + 1]) - 32)
                    i = i + 4
                elif str_input[i] in 'l' and str_input[i + 1] in 'n':
                    str_output = str_output + 'L'
                    i = i + 2
                else:
                    str_output = str_output + str_input[i]
                    i = i + 3
            str_output = str_output + str_input[i]
            i = i + 1
        return str_output

    def __read_symbol(self, symbol):
        if symbol in '(' or not len(self.operators):
            self.operators.append(symbol)
        elif symbol in ')':
            while self.operators[-1] != '(':
                self.__calculations()
            self.operators.pop()
        else:
            while len(self.operators) and self.__priority(self.operators[-1]) >= self.__priority(symbol):
                self.__calculations()
            self.operators.append(symbol)
            
    def __calculations(self):
        result = 0.0
        func = self.operators.pop()
        if self.__priority(func) == 5 or self.__priority(func) == 3:
            a = self.numbers.pop()
            match func:
                case 's':
                    result = math.sin(a)
                case 'c':
                    result = math.cos(a)
                case 't':
                    result = math.tan(a)
                case 'S':
                    result = math.asin(a)
                case 'C':
                    result = math.acos(a)
                case 'T':
                    result = math.atan(a)
                case 'L':
                    result = math.log(a)
                case 'l':
                    result = math.log10(a)
                case 'Q':
                    result = math.sqrt(a)
                case 'u':
                    result = -1 * a
        else:
            a = self.numbers.pop()
            b = self.numbers.pop()
            match func:
                case '+':
                    result = b + a
                case '-':
                    result = b - a
                case '*':
                    result = b * a
                case '/':
                    result = b / a
                case '^':
                    result = b ** a
                case 'm':
                    result = math.fmod(b, a)
        self.numbers.append(result)
 
    def __priority(self, symbol):
        result = 0
        if symbol in "+-":
            result = 1
        elif symbol in "*/m":
            result = 2
        elif symbol in 'u':
            result = 3
        elif symbol in '^':
            result = 4
        elif symbol in "sScCtTlLQ":
            result = 5
        return result



# if __name__ == "__main__":
#     formula = "1+sin(x)"
#     model = ModelCalc()
#     res = model.calculate(formula, 0)
#     print(res)
