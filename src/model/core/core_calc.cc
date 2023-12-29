#include "core_calc.h"

double s21::Calculator::smartcalc(str input, double x) {
  double result = 0;
  stack_num num;
  stack_char oper;
  str output = validation(input);
  str digits = "0123456789.e";
  str number;
  for (size_t i = 0; i < output.size(); i++) {
    if (check_symbol(digits, output[i])) {
      number += output[i];
      if (output[i] == 'e' && (output[i + 1] == '-' || output[i + 1] == '+')) {
        number += output[++i];
      } else if (i == output.size() - 1 ||
                 !check_symbol(digits, output[i + 1])) {
        double temp = 0.0;
        std::istringstream(number) >> temp;
        num.push(temp);
        number.clear();
      }
    } else if (output[i] == 'x') {
      num.push(x);
    } else if (output[i] != 'p') {
      read_char(output[i], num, oper);
    }
  }
  while (!oper.empty()) calculations(num, oper);
  if (!num.empty()) result = num.top();
  return result;
}

s21::str s21::Calculator::validation(str input) {
  str output;
  str symbols = "asctlm";
  str operators = "+-*/(";
  for (size_t i = 0; i < input.size();) {
    if (!i || check_symbol(operators, input[i - 1])) {
      if (input[i] == '-') {
        output += 'u';
        i++;
      } else if (input[i] == '+') {
        output += 'p';
        i++;
      }
    }
    if (check_symbol(symbols, input[i])) check_func(input, output, i);
    if (!check_symbol(symbols, input[i])) output += input[i++];
  }
  return output;
}

bool s21::Calculator::check_symbol(str input, char symbol) {
  bool result = false;
  for (size_t i = 0; i < input.size() && !result; i++)
    if (input[i] == symbol) result = true;
  return result;
}

void s21::Calculator::check_func(str input, str &output, size_t &i) {
  if (input[i] == 'a' || input[i + 1] == 'q') {
    output += (input[i + 1] - 32);
    i += 4;
  } else if (input[i] == 'l' && input[i + 1] == 'n') {
    output += 'L';
    i += 2;
  } else {
    output += input[i];
    i += 3;
  }
}

void s21::Calculator::read_char(char symbol, stack_num &num, stack_char &oper) {
  if (symbol == '(' || oper.empty()) {
    oper.push(symbol);
  } else if (symbol == ')') {
    while (oper.top() != '(') calculations(num, oper);
    oper.pop();
  } else {
    while (!oper.empty() && priority(oper.top()) >= priority(symbol))
      calculations(num, oper);
    oper.push(symbol);
  }
}

void s21::Calculator::calculations(stack_num &num, stack_char &oper) {
  double result = 0;
  char func = oper.top();
  oper.pop();
  if (priority(func) == 5 || priority(func) == 3) {
    double a = num.top();
    num.pop();
    switch (func) {
      case 's':
        result = sin(a);
        break;
      case 'c':
        result = cos(a);
        break;
      case 't':
        result = tan(a);
        break;
      case 'S':
        result = asin(a);
        break;
      case 'C':
        result = acos(a);
        break;
      case 'T':
        result = atan(a);
        break;
      case 'L':
        result = log(a);
        break;
      case 'l':
        result = log10(a);
        break;
      case 'Q':
        result = sqrt(a);
        break;
      case 'u':
        result = -1 * a;
        break;
    }
  } else {
    double a = num.top();
    num.pop();
    double b = num.top();
    num.pop();
    switch (func) {
      case '+':
        result = b + a;
        break;
      case '-':
        result = b - a;
        break;
      case '*':
        result = b * a;
        break;
      case '/':
        result = b / a;
        break;
      case '^':
        result = pow(b, a);
        break;
      case 'm':
        result = fmod(b, a);
        break;
    }
  }
  num.push(result);
}

int s21::Calculator::priority(char sym) {
  int result = 0;
  if (sym == '+' || sym == '-')
    result = 1;
  else if (sym == '*' || sym == '/' || sym == 'm')
    result = 2;
  else if (sym == 'u')
    result = 3;
  else if (sym == '^')
    result = 4;
  else if (sym == 's' || sym == 'c' || sym == 't' || sym == 'l' || sym == 'Q' ||
           sym == 'S' || sym == 'C' || sym == 'T' || sym == 'L')
    result = 5;
  return result;
}
