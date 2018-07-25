import random


class Player:
    def __init__(self, player_type, player_name, match_pile):
        self._type = player_type
        self._name = player_name
        self._match_pile = match_pile

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type


class HumanPlayer(Player):
    def __init__(self, player_name, match_pile):
        Player.__init__(self, "human", player_name, match_pile)

    def _get_user_input(self, query_text):
        return input(query_text)

    def _convert_to_int(self, user_input):
        num = 0
        if user_input == "1":
            num = 1
        elif user_input == "2":
            num = 2
        elif user_input == "3":
            num = 3
        return num

    def _choose_matches(self, matches_left):
        matches_to_remove = 0

        while (matches_left < matches_to_remove or matches_to_remove < 1
               or 3 < matches_to_remove):
            user_input = self._get_user_input(
                "Number of matches to remove (1-3): ")
            matches_to_remove = self._convert_to_int(user_input)

        return matches_to_remove

    def play_turn(self):
        matches_left = self._match_pile.get_remaining_matches()
        matches_to_remove = self._choose_matches(matches_left)
        self._match_pile.remove_matches(matches_to_remove)


class ComputerPlayer(Player):
    def __init__(self, player_name, difficulty, match_pile):
        self._difficulty = difficulty
        Player.__init__(self, "computer", player_name, match_pile)

    def play_turn(self):
        matches_left = self._match_pile.get_remaining_matches()
        choose_randomly = self._determine_randomness(self._difficulty)
        matches_to_remove = self._choose_matches(matches_left, choose_randomly)
        self._match_pile.remove_matches(matches_to_remove)

    def get_difficulty(self):
        return self._difficulty

    def _choose_matches(self, matches_left, choose_randomly):
        if choose_randomly:
            matches_to_remove = random.randint(1, 3)
            while matches_left < matches_to_remove:
                matches_to_remove -= 1
        else:
            for matches_to_remove in reversed(range(1, 4)):
                if not (matches_left - 1 - matches_to_remove) % 4:
                    break
        return matches_to_remove

    def _determine_randomness(self, difficulty):
        choose_randomly = False
        if (difficulty == "easy"
                or difficulty == "medium" and random.randint(0, 1)):
            choose_randomly = True
        return choose_randomly

