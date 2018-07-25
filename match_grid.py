from match_grid_coordinates import Triangle
from match import Match


class MatchGrid:
    def has_match(self, x, y):
        has_match = False
        match = self._grid[(x, y)]
        if isinstance(match, Match):
            if not match.is_removed():
                has_match = True

        return has_match

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def __init__(self, pile_type, matches):
        if pile_type == "triangle":
            grid_coordinates = Triangle()

        self._width, self._height, coordinates = grid_coordinates.calculate(
            len(matches))
        self._grid = self._create_grid()
        self._connect_matches_to_grid(matches, coordinates)

    def _create_grid(self):
        grid = {}
        for x in range(0, self._width):
            for y in range(0, self._height):
                grid[(x, y)] = None

        return grid

    def _connect_matches_to_grid(self, matches, coordinates):
        for match, coordinate in zip(matches, coordinates):
            self._grid[coordinate] = match
