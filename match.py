class Match:
    def __init__(self):
        self._removed = False

    def remove(self):
        self._removed = True

    def is_removed(self):
        return self._removed
