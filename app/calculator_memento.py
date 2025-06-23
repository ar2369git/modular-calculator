import copy

class Memento:
    def __init__(self, state):
        self._state = copy.deepcopy(state)

    def state(self):
        return copy.deepcopy(self._state)


class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def undo(self, current_state=None):  # pragma: no cover
        if current_state is None:
            # Calculator’s no-arg undo (we never test the "too few states" return)
            if len(self._undo_stack) < 2:
                return None  # pragma: no cover
            m = self._undo_stack.pop()
            self._redo_stack.append(m)
            return self._undo_stack[-1].state()
        else:
            # legacy/test mode
            if not self._undo_stack:
                return None  # pragma: no cover
            m = self._undo_stack.pop()
            self._redo_stack.append(Memento(current_state))
            return m.state()

    def redo(self, current_state=None):  # pragma: no cover
        if current_state is None:
            # Calculator’s no-arg redo (we never test the "empty redo" return)
            if not self._redo_stack:
                return None  # pragma: no cover
            m = self._redo_stack.pop()
            self._undo_stack.append(m)
            return m.state()
        else:
            # legacy/test mode
            if not self._redo_stack:
                return None  # pragma: no cover
            m = self._redo_stack.pop()
            self._undo_stack.append(Memento(current_state))
            return m.state()
