from .exceptions import DivideByZeroError

class Operation:
    def execute(self, a, b):
        raise NotImplementedError  # pragma: no cover

class Add(Operation):
    def execute(self, a, b): return a + b

class Subtract(Operation):
    def execute(self, a, b): return a - b

class Multiply(Operation):
    def execute(self, a, b): return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivideByZeroError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b): return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivideByZeroError("Cannot take zeroth root")
        return a ** (1 / b)

class OperationFactory:
    _map = {
        "+": Add,
        "-": Subtract,
        "*": Multiply,
        "/": Divide,
        "^": Power,
        "root": Root,
    }

    @classmethod
    def get(cls, op_symbol):
        op_cls = cls._map.get(op_symbol)
        if not op_cls:
            from .exceptions import InvalidOperationError
            raise InvalidOperationError(f"Unknown operation '{op_symbol}'")
        return op_cls()
