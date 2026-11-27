
import math
import re
from typing import Callable, Optional

import numpy as np
from matplotlib.figure import Figure


class FunctionPlotter:

    _FUNCTIONS: dict[str, tuple[Callable, Optional[Callable]]] = {
        "f(x) = x":      (lambda x: x,          None),
        "f(x) = x²":     (lambda x: x ** 2,     None),
        "f(x) = x³":     (lambda x: x ** 3,     None),
        "f(x) = sin(x)": (np.sin,               None),
        "f(x) = cos(x)": (np.cos,               None),
        "f(x) = eˣ":     (np.exp,               None),
        "f(x) = ln(x)":  (np.log,               lambda x: x > 0),
    }

    # Only digits, operators, brackets, spaces and the word "pi" are allowed
    # in interval fields, so values such as "2*pi" can be typed safely.
    _ALLOWED = re.compile(r"^[0-9+\-*/().\s]*(pi[0-9+\-*/().\s]*)*$|^[0-9+\-*/().\spi]+$")

    def __init__(self, resolution: int = 1000):
        self._resolution = 0
        self.resolution = resolution

        # Result of the last compute() call (used by draw())
        self._x = None
        self._y = None
        self._label = ""
        self._start = 0.0
        self._end = 0.0
        self._warning = None

    # ---------- encapsulated attribute ----------
    @property
    def resolution(self) -> int:
        return self._resolution

    @resolution.setter
    def resolution(self, value: int) -> None:
        if not isinstance(value, int) or value < 2:
            raise ValueError("Resolution must be an integer of at least 2.")
        self._resolution = value

    # ---------- public API ----------
    def get_function_names(self) -> list[str]:
        """Names shown in the GUI combo box."""
        return list(self._FUNCTIONS.keys())

    def parse_number(self, text: str, field_name: str = "Value") -> float:
        """Convert user text (e.g. '3.5', '-2', '2*pi') to a finite float."""
        text = (text or "").strip()
        if not text:
            raise ValueError(f"{field_name} is empty. Please enter a number.")
        if not self._ALLOWED.match(text):
            raise ValueError(
                f"{field_name} '{text}' is not a valid number. "
                "Use digits or expressions such as 2*pi.")
        try:
            value = float(eval(text, {"__builtins__": {}}, {"pi": math.pi}))
        except Exception:
            raise ValueError(f"{field_name} '{text}' is not a valid number.")
        if not math.isfinite(value):
            raise ValueError(f"{field_name} must be a finite number.")
        return value

    def compute(self, function_name: str, start: float, end: float) -> None:
        """Compute the valid (x, y) points of the chosen function on [start, end]
        and store them in the object for draw() to use."""
        if function_name not in self._FUNCTIONS:
            raise ValueError("Please select a function to plot.")
        if start >= end:
            raise ValueError(
                "Invalid interval: the starting value must be smaller "
                "than the ending value.")

        func, domain = self._FUNCTIONS[function_name]
        x = np.linspace(start, end, self._resolution)

        warning = None
        if domain is not None:
            mask = domain(x)
            if not mask.any():
                raise ValueError(
                    f"{function_name} is not defined anywhere on "
                    f"[{start:g}, {end:g}]. (ln(x) needs x > 0.)")
            if not mask.all():
                warning = ("Part of the interval is outside the domain of the "
                           "function (x ≤ 0). Only the valid part is plotted.")
            x = x[mask]

        with np.errstate(all="ignore"):       # silence overflow / log warnings
            y = func(x)

        finite = np.isfinite(y)
        if not finite.any():
            raise ValueError("The function has no finite values on this interval.")
        if not finite.all():
            warning = "Some points overflowed and were skipped."
            x, y = x[finite], y[finite]

        self._x, self._y = x, y
        self._label = function_name
        self._start, self._end = start, end
        self._warning = warning

    def draw(self, figure: Figure) -> None:
        """Draw the last computed curve onto the given Matplotlib figure."""
        if self._x is None:
            raise ValueError("Nothing to draw yet. Compute a function first.")
        figure.clear()
        ax = figure.add_subplot(111)
        ax.plot(self._x, self._y, linewidth=2, label=self._label)
        ax.axhline(0, color="black", linewidth=0.8)   # horizontal axis
        ax.axvline(0, color="black", linewidth=0.8)   # vertical axis
        ax.set_xlim(self._start, self._end)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title(f"{self._label}    ({self._start:g} ≤ x ≤ {self._end:g})")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(loc="best")
        figure.tight_layout()

    def plot(self, figure: Figure, function_name: str,
             start_text: str, end_text: str) -> Optional[str]:
        """Convenience method used by the GUI: parse -> compute -> draw.

        Returns a warning string (or None). Raises ValueError on invalid input.
        """
        start = self.parse_number(start_text, "Starting value")
        end = self.parse_number(end_text, "Ending value")
        self.compute(function_name, start, end)
        self.draw(figure)
        return self._warning
