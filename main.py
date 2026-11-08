
import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction

from gui.main_window import Ui_MainWindow
from calculator.engines import CalculatorEngine, TrigonometryEngine, InputValidator


class CalculatorApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # Setup the UI created by Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Our team's calculator engines
        self.calcEngine = CalculatorEngine()
        self.trigEngine = TrigonometryEngine()
        self.validator = InputValidator()

        # Application State Variables
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.last_answer = 0.0
        self.start_new_input = False

        self.ui.btn_anglemode.setText("DEG")

        # Connect Buttons to Methods
        self.connect_signals()
        self.setup_trig_menu()

    def connect_signals(self):

        # Numbers
        self.ui.btn_0.clicked.connect(lambda: self.append_number("0"))
        self.ui.btn_1.clicked.connect(lambda: self.append_number("1"))
        self.ui.btn_2.clicked.connect(lambda: self.append_number("2"))
        self.ui.btn_3.clicked.connect(lambda: self.append_number("3"))
        self.ui.btn_4.clicked.connect(lambda: self.append_number("4"))
        self.ui.btn_5.clicked.connect(lambda: self.append_number("5"))
        self.ui.btn_6.clicked.connect(lambda: self.append_number("6"))
        self.ui.btn_7.clicked.connect(lambda: self.append_number("7"))
        self.ui.btn_8.clicked.connect(lambda: self.append_number("8"))
        self.ui.btn_9.clicked.connect(lambda: self.append_number("9"))
        self.ui.btn_dot.clicked.connect(lambda: self.append_number("."))

        # Constants
        self.ui.btn_pi.clicked.connect(lambda: self.insert_constant(math.pi))
        self.ui.btn_e.clicked.connect(lambda: self.insert_constant(math.e))
        self.ui.btn_ans.clicked.connect(self.insert_ans)

        # Basic Math Operations
        self.ui.btn_add.clicked.connect(lambda: self.set_operation("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.set_operation("-"))
        self.ui.btn_mlt.clicked.connect(lambda: self.set_operation("*"))
        self.ui.btn_div.clicked.connect(lambda: self.set_operation("/"))

        # Power Operation
        self.ui.btn_power.clicked.connect(lambda: self.set_operation("^"))

        # Unary Math Operations
        self.ui.btn_root.clicked.connect(lambda: self.calculate_unary("root"))
        self.ui.btn_log.clicked.connect(lambda: self.calculate_unary("log"))
        self.ui.btn_ln.clicked.connect(lambda: self.calculate_unary("ln"))
        self.ui.btn_exp.clicked.connect(lambda: self.calculate_unary("exp"))

        # Actions
        self.ui.btn_equal.clicked.connect(self.calculate_result)
        self.ui.btn_c.clicked.connect(self.clear_screen)
        self.ui.btn_del.clicked.connect(self.backspace)
        self.ui.btn_anglemode.clicked.connect(self.toggle_angle_mode)
        self.ui.btn_sign.clicked.connect(self.toggle_sign)

    def setup_trig_menu(self):

        trig_menu = QMenu(self)
        trig_menu.setStyleSheet("font-size: 20px; padding: 10px;")

        actions = [
            ("sin", "sin"),
            ("cos", "cos"),
            ("tan", "tan"),
            ("sin⁻¹ (arcsin)", "asin"),
            ("cos⁻¹ (arccos)", "acos"),
            ("tan⁻¹ (arctan)", "atan")
        ]

        for label, func in actions:
            action = QAction(label, self)
            action.triggered.connect(
                lambda checked=False, f=func: self.calculate_trig(f)
            )
            trig_menu.addAction(action)

        self.ui.btn_Trigonometry.setMenu(trig_menu)

    # Error Handling
    def show_error(self, message):

        self.ui.lbl_display.setText(message)
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.start_new_input = True

    # Number Input
    def append_number(self, num):

        if self.start_new_input:
            self.current_input = ""
            self.start_new_input = False

        if num == ".":
            if "." in self.current_input:
                return

            if self.current_input == "":
                self.current_input = "0"

        if self.current_input == "0" and num != ".":
            self.current_input = num
        else:
            self.current_input += num

        self.ui.lbl_display.setText(self.current_input)

    # Constants
    def insert_constant(self, val):

        self.current_input = str(val)
        self.start_new_input = False
        self.ui.lbl_display.setText(self.current_input)

    # Answer Button
    def insert_ans(self):

        self.current_input = str(self.last_answer)
        self.start_new_input = False
        self.ui.lbl_display.setText(self.current_input)

    # Change Sign
    def toggle_sign(self):

        if self.current_input == "" or self.current_input == "0":
            return

        if self.current_input.startswith("-"):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = "-" + self.current_input

        self.start_new_input = False
        self.ui.lbl_display.setText(self.current_input)

    # Select Operation
    def set_operation(self, op):

        if self.current_input != "":
            self.previous_input = self.current_input
            self.current_input = ""
            self.operation = op
            self.start_new_input = False

    # Display the Result
    def display_result(self, result):

        if isinstance(result, complex) or not math.isfinite(result):
            raise ValueError("Invalid mathematical result.")

        self.ui.lbl_display.setText(str(result))
        self.current_input = str(result)
        self.previous_input = ""
        self.operation = None
        self.last_answer = result
        self.start_new_input = True

    # Basic Calculations
    def calculate_result(self):

        if self.previous_input == "" or self.current_input == "" or self.operation is None:
            return

        try:
            a = float(self.previous_input)
            b = float(self.current_input)

            if self.operation == "+":
                result = self.calcEngine.Add(a, b)

            elif self.operation == "-":
                result = self.calcEngine.Subtract(a, b)

            elif self.operation == "*":
                result = self.calcEngine.Multiply(a, b)

            elif self.operation == "^":
                result = self.calcEngine.Power(a, b)

            elif self.operation == "/":
                if not self.validator.validateNonZero(b):
                    raise ValueError("Division by zero is not allowed.")

                result = self.calcEngine.Divide(a, b)

            else:
                return

            self.display_result(result)

        except (ValueError, OverflowError, ZeroDivisionError) as error:
            self.show_error("Error: " + str(error))

    # Scientific Calculations
    def calculate_unary(self, op):

        if self.current_input == "":
            return

        try:
            value = float(self.current_input)

            if op == "root":
                if not self.validator.validateSquareRoot(value):
                    raise ValueError("Cannot take the square root of a negative number.")

                result = self.calcEngine.SquareRoot(value)

            elif op == "log":
                if not self.validator.validateLog(value):
                    raise ValueError("Logarithm requires a positive number.")

                result = self.calcEngine.Logarithm(value)

            elif op == "ln":
                if not self.validator.validateLog(value):
                    raise ValueError("Natural logarithm requires a positive number.")

                result = self.calcEngine.Ln(value)

            elif op == "exp":
                result = self.calcEngine.Exp(value)

            else:
                return

            self.display_result(result)

        except (ValueError, OverflowError, ZeroDivisionError) as error:
            self.show_error("Error: " + str(error))

    # Trigonometry Calculations
    def calculate_trig(self, func):

        if self.current_input == "":
            return

        try:
            value = float(self.current_input)

            if func in ("asin", "acos"):
                if not self.validator.validateInverseTrig(value):
                    raise ValueError("Inverse trig input must be between -1 and 1.")

            if func == "sin":
                result = self.trigEngine.Sin(value)

            elif func == "cos":
                result = self.trigEngine.Cos(value)

            elif func == "tan":
                result = self.trigEngine.Tan(value)

            elif func == "asin":
                result = self.trigEngine.ArcSin(value)

            elif func == "acos":
                result = self.trigEngine.ArcCos(value)

            elif func == "atan":
                result = self.trigEngine.ArcTan(value)

            else:
                return

            self.display_result(result)

        except (ValueError, OverflowError, ZeroDivisionError) as error:
            self.show_error("Error: " + str(error))

    # Degree and Radian Modes
    def toggle_angle_mode(self):

        if self.trigEngine.angleMode == "Degree":
            self.trigEngine.SetAngleMode("Radian")
            self.ui.btn_anglemode.setText("RAD")

        else:
            self.trigEngine.SetAngleMode("Degree")
            self.ui.btn_anglemode.setText("DEG")

    # Clear Button
    def clear_screen(self):

        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.start_new_input = False
        self.ui.lbl_display.setText("0")

    # Delete Button
    def backspace(self):

        self.current_input = self.current_input[:-1]
        self.start_new_input = False

        if self.current_input == "":
            self.ui.lbl_display.setText("0")
        else:
            self.ui.lbl_display.setText(self.current_input)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()

    sys.exit(app.exec_())
