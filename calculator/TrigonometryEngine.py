import math
class TrigonometryEngine:
   def __init__(self):
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
       return math.tan(value)

   def ArcSin(self, value):
       result = math.asin(value)
       if self.__angleMode == "Degree":
          result = math.degrees(result)
       return result

   def ArcCos(self, value):
       result = math.acos(value)
       if self.__angleMode == "Degree":
          result = math.degrees(result)
       return result

   def ArcTan(self, value):
       result = math.atan(value)
       if self.__angleMode == "Degree":
          result = math.degrees(result)
       return result
