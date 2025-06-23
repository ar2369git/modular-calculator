import sys
from .calculation import Calculator
from .input_validators import parse_number, parse_command
from .exceptions import CalculatorError, ConfigError

def print_help():
    help_text = """
Commands:
  <num> <op> <num>    perform calculation (ops: +, -, *, /, ^, root)
  history             show past calculations
  undo                undo last operation
  redo                redo last undone operation
  save                save history immediately
  load                reload history from disk
  clear               clear screen
  help                show this help
  exit                quit
"""
    print(help_text)

def main():
    try:
        calc = Calculator()
    except ConfigError:
        calc = None

    print("Modular Calculator. Type 'help' for commands.")
    while True:
        try:
            raw = input("> ").strip()
            if not raw:
                continue
            tokens = raw.split()
            cmd, _ = parse_command(tokens)

            if cmd in ("exit", "quit"):
                break
            elif cmd == "help":
                print_help()
            elif cmd == "history":
                if calc:
                    print(calc.history.df.to_string(index=False))
                else:
                    print("(no history available)")  # pragma: no cover
            elif cmd == "undo":
                if calc:
                    res = calc.undo()
                    print("Reverted to:", res)
            elif cmd == "redo":
                if calc:
                    res = calc.redo()
                    print("Redo result:", res)
            elif cmd == "save":
                if calc:
                    calc.history.save()
                    print("History saved.")  # pragma: no cover
            elif cmd == "load":
                if calc:
                    calc.history.load()
                    print("History reloaded.")  # pragma: no cover
            elif cmd == "clear":
                sys.stdout.write("\x1b[2J\x1b[H")  # pragma: no cover
            else:
                if len(tokens) != 3:
                    raise CalculatorError("Usage: <num> <op> <num>")  # pragma: no cover
                a = parse_number(tokens[0])
                op = tokens[1]
                b = parse_number(tokens[2])
                if not calc:
                    raise CalculatorError("Calculator not configured")  # pragma: no cover
                result = calc.calculate(op, a, b)
                print(result)

        except CalculatorError as e:
            print("Error:", e)
        except KeyboardInterrupt:
            print("\nExiting.")  # pragma: no cover
            break  # pragma: no cover

if __name__ == "__main__":
    main()
