import random


class Player:
    def __init__(self, player_type, player_name, match_pile):
        self._type = player_type
        self._name = player_name
        self._match_pile = match_pile

    @staticmethod
    def create(config, match_pile):
        if config['type'] == 'human':
            return HumanPlayer(config['name'], match_pile)
        elif config['type'] == 'computer':
            return ComputerPlayer(config['name'], config['difficulty'],
                                  match_pile)

    def play_turn(self):
        matches_left = self._match_pile.get_remaining_matches()
        matches_to_remove = self._choose_matches(matches_left)
        self._match_pile.remove_matches(matches_to_remove)

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def _choose_matches(self, matches_left):
        pass


class HumanPlayer(Player):
    def __init__(self, player_name, match_pile):
        Player.__init__(self, "human", player_name, match_pile)

    def _get_verified_user_input(self, query_text, allowed_input):
        user_input = ''
        while user_input not in allowed_input:
            user_input = self._get_user_input(query_text)

        return user_input

    def _get_user_input(self, query_text):
        return input(query_text)

    def _choose_matches(self, matches_left):
        matches_to_remove = 0

        while not matches_to_remove or matches_left < matches_to_remove:
            user_input = self._get_verified_user_input(
                "Number of matches to remove (1-3): ", ['1', '2', '3'])
            matches_to_remove = int(user_input)

        return matches_to_remove


class ComputerPlayer(Player):
    def __init__(self, player_name, difficulty, match_pile):
        self._difficulty = difficulty
        Player.__init__(self, "computer", player_name, match_pile)

    def get_difficulty(self):
        return self._difficulty

    def _choose_matches(self, matches_left):
        choose_randomly = self._determine_randomness(self._difficulty)

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
