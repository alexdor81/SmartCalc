#include <pybind11/pybind11.h>

#include "core_calc.h"

namespace py = pybind11;

PYBIND11_MODULE(calculator_lib, m) {
    py::class_<s21::Calculator>(m, "Calculator")
    .def(py::init())
    .def("smartcalc", &s21::Calculator::smartcalc);
};
