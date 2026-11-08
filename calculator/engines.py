
import math


class InputValidator:
    def __init__(self):
        self.__ErrorMessage = ""

    def validateNonZero(self, value):
        return value != 0

    def validateSquareRoot(self, value):
        return value >= 0

    def validateLog(self, value):
        return value > 0

    def validateInverseTrig(self, value):
        return -1 <= value <= 1


class CalculatorEngine:
    def __init__(self):
        self.__answer = 0.0

    def Add(self, a, b):
        return a + b

    def Subtract(self, a, b):
        return a - b

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def Power(self, base, exp):
        return math.pow(base, exp)

    def SquareRoot(self, value):
        return math.sqrt(value)

    def Logarithm(self, value):
        return math.log10(value)

    def Ln(self, value):
        return math.log(value)

    def Exp(self, value):
        return math.exp(value)


# Inheritance: TrigonometryEngine is the child class
class TrigonometryEngine(CalculatorEngine):

    def __init__(self):
        super().__init__()
        self.__angleMode = "Degree"

    @property
    def angleMode(self):
        return self.__angleMode

    def SetAngleMode(self, mode):
        if mode not in ("Degree", "Radian"):
            raise ValueError("Invalid angle mode.")
        self.__angleMode = mode

    def _convert_to_radians(self, value):
        if self.__angleMode == "Degree":
            return math.radians(value)
        return value

    def _convert_from_radians(self, value):
        if self.__angleMode == "Degree":
            return math.degrees(value)
        return value

    def Sin(self, value):
        return math.sin(self._convert_to_radians(value))

    def Cos(self, value):
        return math.cos(self._convert_to_radians(value))

    def Tan(self, value):
        angle = self._convert_to_radians(value)

        if abs(math.cos(angle)) < 1e-12:
            raise ValueError("Tangent is undefined for this angle.")

        return math.tan(angle)

    def ArcSin(self, value):
        result = math.asin(value)
        return self._convert_from_radians(result)

    def ArcCos(self, value):
        result = math.acos(value)
        return self._convert_from_radians(result)

    def ArcTan(self, value):
        result = math.atan(value)
        return self._convert_from_radians(result)
