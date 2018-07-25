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


class Match:
    def __init__(self):
        self._removed = False

    def remove(self):
        self._removed = True

    def is_removed(self):
        return self._removed


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


class GridCoordinates:
    pass


class Triangle(GridCoordinates):
    def calculate(self, number_of_matches):
        matches_in_rows = self._calculate_matches_in_rows(number_of_matches)
        width, height = self._get_size(matches_in_rows)
        return width, height, self._calculate_coordinates(matches_in_rows)

    def _calculate_matches_in_rows(self, number_of_matches):
        if not number_of_matches:
            return []

        number_of_rows = 1
        row = 0
        matches_in_rows = [0]

        for i in range(0, number_of_matches):
            if row != 0:
                matches_in_rows[row] += 1
                row -= 1
            else:
                if matches_in_rows[row] < 2:
                    matches_in_rows[row] += 1
                else:
                    number_of_rows += 1
                    matches_in_rows[1:] = matches_in_rows
                    matches_in_rows[0] = 1
                    row = number_of_rows - 1
        return matches_in_rows

    def _calculate_coordinates(self, matches_in_rows):
        if not matches_in_rows:
            return []

        number_of_rows = len(matches_in_rows)
        matches_in_last_row = matches_in_rows[number_of_rows - 1]
        match_coordinates = []

        for row, matches_in_row in enumerate(matches_in_rows):
            for column in range(0, matches_in_row):
                match_x = matches_in_last_row - matches_in_row + 2*column
                match_y = row
                match_coordinates.append((match_x, match_y))

        return match_coordinates

    def _get_size(self, matches_in_rows):
        if not matches_in_rows:
            return 0, 0

        height = len(matches_in_rows)
        width = 2*matches_in_rows[height - 1] - 1
        return width, height
