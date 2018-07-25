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
