import math
from CalculatorEngine import CalculatorEngine
class TrigonometryEngine(CalculatorEngine):
   def __init__(self):
       super().__init__()
       self.__angleMode = "Degree"
   def SetAngleMode(self, mode):
       self.__angleMode = mode

   def Sin(self, value):
       if self.__angleMode == "Degree":
           value = math.radians(value)
       return math.sin(value)

   def Cos(self, value):
       if self.__angleMode == "Degree":
           value = math.radians(value)
       return math.cos(value)

   def Tan(self, value):
       if self.__angleMode == "Degree":
           value = math.radians(value)
       if round(math.cos(value), 10) == 0:
           raise ValueError("Tangent is undefined for this angle.")
       return math.tan(value)

   def ArcSin(self, value):
       if value < -1 or value > 1:
           raise ValueError("ArcSin input must be between -1 and 1.")
       result = math.asin(value)
       if self.__angleMode == "Degree":
           result = math.degrees(result)
       return result

   def ArcCos(self, value):
       if value < -1 or value > 1:
           raise ValueError("ArcCos input must be between -1 and 1.")
       result = math.acos(value)
       if self.__angleMode == "Degree":
           result = math.degrees(result)
       return result

   def ArcTan(self, value):
       result = math.atan(value)
       if self.__angleMode == "Degree":
           result = math.degrees(result)
       return result
