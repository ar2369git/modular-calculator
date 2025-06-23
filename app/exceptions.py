class CalculatorError(Exception):
    """Base class for calculator exceptions."""

class DivideByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

class InvalidOperationError(CalculatorError):
    """Raised when an unknown operation is requested."""

class ConfigError(CalculatorError):
    """Raised when configuration is missing or invalid."""
