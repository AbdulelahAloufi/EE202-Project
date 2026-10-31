import math


class CalculatorEngine:

  def __init__(self,answer):
    self.__answer = 0.0

  def Add(self, a, b):
    self.__answer = a + b
    return self.__answer

  def Subtract(self, a, b):
    self.__answer = a - b
    return self.__answer

  def Multiply(self, a, b):
    self.__answer = a * b
    return self.__answer

  def Divide(self, a, b):
    if b == 0:
      raise ValueError("Division by zero is not allowed.")
    self.__answer = a / b
    return self.__answer

  def Power(self, base, exp):
    self.__answer = base**exp
    return self.__answer

  def SquareRoot(self, value):
    if value < 0:
      raise ValueError("Cannot take the square root of a negative number.")
    self.__answer = math.sqrt(value)
    return self.__answer

  def ChangeSign(self, value):
    self.__answer = -value
    return self.__answer

  def Logarithm(self, value):
    if value <= 0:
      raise ValueError("Logarithm is only defined for strictly positive numbers.")
    self.__answer = math.log10(value)
    return self.__answer

  def Ln(self, value):
    if value <= 0:
      raise ValueError("Natural logarithm is only defined for strictly positive numbers.")
    self.__answer = math.log(value)
    return self.__answer

  def Exponential(self, value):
    self.__answer = math.exp(value)
    return self.__answer

  def Reset(self):
    self.__answer = 0.0
