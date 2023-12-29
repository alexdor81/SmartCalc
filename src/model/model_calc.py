from model.core import calculator_lib


class ModelCalc:

    @staticmethod
    def calculate(str_input, x):
        model_c = calculator_lib.Calculator()
        return model_c.smartcalc(str_input, x)
