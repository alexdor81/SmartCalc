#pragma once

#include <cmath>
#include <iostream>
#include <limits>
#include <sstream>
#include <stack>
#include <string>

namespace s21 {

using stack_num = std::stack<double>;
using stack_char = std::stack<char>;
using str = std::string;

class Calculator {
 public:
  double smartcalc(str input, double x);

 private:
  str validation(str input);
  bool check_symbol(str input, char symbol);
  void check_func(str input, str &output, size_t &i);
  void read_char(char symbol, stack_num &num, stack_char &oper);
  void calculations(stack_num &num, stack_char &oper);
  int priority(char sym);
};

}  // namespace s21
