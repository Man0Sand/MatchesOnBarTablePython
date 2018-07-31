from enum import Enum


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
        self._output_to_screen(self._drawing.draw())

    def _output_to_screen(self, output):
        print(output)


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
        elif pile_type == "square":
            grid_coordinates = Square()
        else:
            grid_coordinates = None

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
    class State(Enum):
        ADD_NEW_ROW = 1
        GROW_FIRST_ROW = 2
        GROW_OTHER_ROWS = 3

    def calculate(self, number_of_matches):
        matches_in_rows = self._calculate_matches_in_rows(number_of_matches)
        width, height = self._get_size(matches_in_rows)
        return width, height, self._calculate_coordinates(matches_in_rows)

    def _calculate_matches_in_rows(self, number_of_matches):
        pass

    def _get_width(self, matches_in_last_row):
        pass

    def _calculate_x_coordinate(self, column, matches_in_row,
                                matches_in_last_row):
        pass

    def _get_size(self, matches_in_rows):
        if not matches_in_rows:
            return 0, 0

        height = len(matches_in_rows)
        width = self._get_width(matches_in_rows[-1])
        return width, height

    def _calculate_coordinates(self, matches_in_rows):
        match_coordinates = []

        for row, matches_in_row in enumerate(matches_in_rows):
            for column in range(0, matches_in_row):
                match_x = self._calculate_x_coordinate(column, matches_in_row,
                                                       matches_in_rows[-1])
                match_y = row
                match_coordinates.append((match_x, match_y))

        return match_coordinates


class Triangle(GridCoordinates):
    def _calculate_matches_in_rows(self, number_of_matches):
        row = None
        next_state = None
        matches_in_rows = []

        for i in range(0, number_of_matches):
            if i == 0:
                state = self.State.ADD_NEW_ROW
            else:
                state = next_state

            if state == self.State.ADD_NEW_ROW:
                matches_in_rows.insert(0, 1)
                row = -1
                next_state = self.State.GROW_OTHER_ROWS
            if state == self.State.GROW_OTHER_ROWS:
                matches_in_rows[row] += 1
                if matches_in_rows[0] == 2:
                    next_state = self.State.ADD_NEW_ROW
                else:
                    row -= 1

        return matches_in_rows

    def _calculate_x_coordinate(self, column, matches_in_row,
                                matches_in_last_row):
        return matches_in_last_row - matches_in_row + 2 * column

    def _get_width(self, matches_in_last_row):
        return 2*matches_in_last_row - 1


class Square(GridCoordinates):
    def _calculate_matches_in_rows(self, number_of_matches):
        row = None
        next_state = None
        matches_in_rows = []

        for i in range(number_of_matches):
            if i == 0:
                state = self.State.ADD_NEW_ROW
            elif i == 1:
                row = 0
                state = self.State.GROW_OTHER_ROWS
            else:
                state = next_state

            if state == self.State.ADD_NEW_ROW:
                matches_in_rows.insert(0, 1)
                next_state = self.State.GROW_FIRST_ROW
            elif state == self.State.GROW_FIRST_ROW:
                matches_in_rows[0] += 1
                if matches_in_rows[0] == len(matches_in_rows):
                    row = -1
                    next_state = self.State.GROW_OTHER_ROWS
            elif state == self.State.GROW_OTHER_ROWS:
                matches_in_rows[row] += 1
                if matches_in_rows[0] == len(matches_in_rows) + 1:
                    next_state = self.State.ADD_NEW_ROW
                else:
                    row -= 1

        return matches_in_rows

    def _calculate_x_coordinate(self, column, matches_in_row,
                                matches_in_last_row):
        return column

    def _get_width(self, matches_in_last_row):
        return matches_in_last_row
