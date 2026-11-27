
import math


class EquationSolver:

    def __init__(self):
        self.__a1 = None
        self.__b1 = None
        self.__c1 = None

        self.__a2 = None
        self.__b2 = None
        self.__c2 = None

        self.__x = None
        self.__y = None

    def set_equations(self, a1, b1, c1, a2, b2, c2):

        try:
            values = [float(v) for v in
                      (a1, b1, c1, a2, b2, c2)]

        except (ValueError, TypeError):
            raise ValueError("Please enter valid numbers.")

        if not all(math.isfinite(v) for v in values):
            raise ValueError("Please enter finite numbers.")

        (self.__a1, self.__b1, self.__c1,
         self.__a2, self.__b2, self.__c2) = values

        self.__x = None
        self.__y = None

    def determinant(self):

        if self.__a1 is None:
            raise ValueError("Enter equations first.")

        return self.__a1 * self.__b2 - self.__a2 * self.__b1

    def solve(self):

        d = self.determinant()

        if math.isclose(d, 0.0, abs_tol=1e-12):
            raise ValueError("No unique solution exists.")

        x = (self.__c1 * self.__b2 -
             self.__c2 * self.__b1) / d

        y = (self.__a1 * self.__c2 -
             self.__a2 * self.__c1) / d

        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError("Invalid result.")

        self.__x = x
        self.__y = y

    def get_x(self):

        if self.__x is None:
            raise ValueError("Solve equations first.")

        return self.__x

    def get_y(self):

        if self.__y is None:
            raise ValueError("Solve equations first.")

        return self.__y
