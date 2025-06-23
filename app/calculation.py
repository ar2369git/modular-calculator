from .operations import OperationFactory
from .history import HistoryManager
from .calculator_memento import Caretaker
from .calculator_config import Config
from .exceptions import CalculatorError

class Calculator:
    def __init__(self):
        Config.validate()
        self.history = HistoryManager(Config.HISTORY_PATH)
        self._caretaker = Caretaker()
        self._last_result = None
        # save initial (empty) state
        self._caretaker.save(self._snapshot())

    def _snapshot(self):
        # copy DataFrame to avoid aliasing
        return {
            "history": self.history.df.copy(),
            "last_result": self._last_result
        }

    def _restore(self, state):
        self.history.df = state["history"].copy()
        self._last_result = state["last_result"]

    def calculate(self, op_symbol, a, b):
        # coerce to float so expr always shows 2.0 + 3.0 etc.
        a_f = float(a)
        b_f = float(b)

        op = OperationFactory.get(op_symbol)
        result = op.execute(a_f, b_f)

        expr = f"{a_f} {op_symbol} {b_f}"
        self._last_result = result

        self.history.add(expr, result)
        if Config.AUTO_SAVE:
            self.history.save()

        # capture new state for undo/redo
        self._caretaker.save(self._snapshot())
        return result

    def undo(self):  # pragma: no cover
        state = self._caretaker.undo()
        if state is not None:
            self._restore(state)
            return self._last_result
        return None

    def redo(self):  # pragma: no cover
        state = self._caretaker.redo()
        if state is not None:
            self._restore(state)
            return self._last_result
        return None
