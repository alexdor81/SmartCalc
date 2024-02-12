import string
from pathlib import Path
import numpy
import pyqtgraph
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QGraphicsScene
from model.model_calc import ModelCalc


class GraphWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).resolve().parent / "graphwindow.ui", self)
        self.setWindowTitle("GraphView")
        self.model = ModelCalc()
        self.plt = pyqtgraph.PlotWidget()
        self.plt.setBackground("w")
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.plt)
        self.pushButton_build.clicked.connect(self.build_graph)

    def set_formula(self, formula):
        self.plt.clear()
        self.graphics_view.setScene(self.scene)
        self.label_function.setText(formula)

    def build_graph(self):
        formula = self.label_function.text()
        if self.check_formula(formula):
            x_begin = self.x_min.value()
            x_end = self.x_max.value()
            y_begin = self.y_min.value()
            y_end = self.y_max.value()
            self.plt.setXRange(x_begin, x_end)
            self.plt.setYRange(y_begin, y_end)
            x_value = numpy.linspace(x_begin, x_end, 10000)
            y_value = numpy.array([self.model.calculate(formula, x) for x in x_value])
            self.plt.showGrid(x=True, y=True, alpha=1.0)
            self.plt.plot(x_value, y_value, symbol="o", symbolSize=0.5, symbolBrush="b")

    def check_formula(self, formula):
        res = True
        lst = list(formula)
        bracket = lst.count(")") - lst.count("(")
        if not formula or bracket or formula[-1] not in string.digits + "x)":
            res = False
            self.label_function.setText("Error")
        return res
