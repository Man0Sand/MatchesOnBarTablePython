from match import Match
from match_drawing import MatchDrawing


class MatchPile:
    def __init__(self, matches_at_start, pile_type):
        self._matches = [Match() for i in range(0, matches_at_start)]
        self._active_match = iter(self._matches)
        self._drawing = MatchDrawing(pile_type, self._matches)

    def get_remaining_matches(self):
        matches_left = 0
        for match in self._matches:
            if not match.is_removed():
                matches_left += 1

        return matches_left

    def remove_matches(self, matches_to_remove):
        if matches_to_remove < 0:
            return

        if matches_to_remove <= self.get_remaining_matches():
            for i in range(matches_to_remove):
                next(self._active_match).remove()

    def print_matches(self):
        print(self._drawing.draw())
