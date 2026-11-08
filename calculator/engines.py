import math

class InputValidator:
    def __init__(self):
        self.ErrorMessage = ""

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
        self.answer = 0.0

    def Add(self, a, b): return a + b
    def Subtract(self, a, b): return a - b
    def Multiply(self, a, b): return a * b
    def Divide(self, a, b): return a / b
    def Power(self, base, exp): return math.pow(base, exp)
    def SquareRoot(self, value): return math.sqrt(value)
    def Logarithm(self, value): return math.log10(value)
    def Ln(self, value): return math.log(value)
    def Exp(self, value): return math.exp(value)

class TrigonometryEngine:
    def __init__(self):
        self.angleMode = "Degree"

    def SetAngleMode(self, mode):
        self.angleMode = mode

    def _convert_to_radians(self, value):
        return math.radians(value) if self.angleMode == "Degree" else value

    def _convert_from_radians(self, value):
        return math.degrees(value) if self.angleMode == "Degree" else value

    def Sin(self, value): return math.sin(self._convert_to_radians(value))
    def Cos(self, value): return math.cos(self._convert_to_radians(value))
    def Tan(self, value): return math.tan(self._convert_to_radians(value))
    
    def ArcSin(self, value): return self._convert_from_radians(math.asin(value))
    def ArcCos(self, value): return self._convert_from_radians(math.acos(value))
    def ArcTan(self, value): return self._convert_from_radians(math.atan(value))
