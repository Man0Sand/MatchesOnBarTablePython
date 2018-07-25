from match_grid import MatchGrid


class MatchDrawing:
    MATCH = "I"
    EMPTY = " "

    def __init__(self, pile_type, matches):
        self._grid = MatchGrid(pile_type, matches)

    def draw(self):
        match_pile = ""
        for y in range(self._grid.get_height()):
            for x in range(self._grid.get_width()):
                if self._grid.has_match(x, y):
                    match_pile += MatchDrawing.MATCH
                else:
                    match_pile += MatchDrawing.EMPTY
            match_pile += "\n"

        return match_pile
