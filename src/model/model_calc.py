import string


class ModelCalc:

    def __int__(self):
        self.lst_numbers = []
        self.lst_operators = []

    def calculate(self, str_input, x):
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
                    self.lst_numbers.append(float(number))
                    number = ""
            elif str_output == 'x':
                self.lst_numbers.append(x)
            else:
                self.read_symbol(str_output[i])

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
                if str_input[i] == 'a' or str_input[i + 1] == 'q':
                    str_output = str_output + chr(ord(str_input[i + 1]) - 32)
                    i = i + 4
                elif str_input[i] == 'l' and str_input[i + 1] == 'n':
                    str_output = str_output + 'L'
                    i = i + 2
                else:
                    str_output = str_output + str_input[i]
                    i = i + 3
            str_output = str_output + str_input[i]
            i = i + 1
        return str_output

    def read_symbol(symbol, numbers, operators):
    #     if symbol == '(' or not len(operators):
    #         operators.append(symbol)
    #     elif symbol == ')':
    #         while operators[-1] != '(':
    #             ModelCalc.calculations(numbers, operators)
    #         operators.pop()
    #     else:
    #         while len(operators) and ModelCalc.p



if __name__ == "__main__":
    formula = "+1e+23+23*sin(cos(230))/atan(-x)-sqrt(-3+763--4)+6mod3"
    res = ModelCalc.validation(formula)
    print(res)
