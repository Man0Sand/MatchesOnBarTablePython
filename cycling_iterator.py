class CyclingIterator:
    def __init__(self, iteratee):
        self._iteratee = iteratee
        self._iterator = iter(self._iteratee)

    def advance(self):
        try:
            active_element = next(self._iterator)
        except StopIteration:
            self._iterator = iter(self._iteratee)
            active_element = next(self._iterator)
        return active_element
