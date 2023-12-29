from model.model_calc import ModelCalc


class Presenter:

    @staticmethod
    def calculate(str_input, x):
        return ModelCalc.calculate(str_input, x)
