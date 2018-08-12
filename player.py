import random


class Player:
    def __init__(self, player_type, player_name):
        self._type = player_type
        self._name = player_name

    @staticmethod
    def create(config):
        if config['type'] == 'human':
            return HumanPlayer(config['name'])
        elif config['type'] == 'computer':
            return ComputerPlayer(config['name'], config['difficulty'])

    def play_round(self, matches_left):
        pass

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type


class HumanPlayer(Player):
    def __init__(self, player_name):
        Player.__init__(self, "human", player_name)

    def _get_verified_user_input(self, query_text, allowed_input):
        user_input = ''
        while user_input not in allowed_input:
            user_input = self._get_user_input(query_text)

        return user_input

    def _get_user_input(self, query_text):
        return input(query_text)

    def _output_to_screen(self, output):
        print(output)

    def play_round(self, matches_left):
        matches_to_remove = 0

        while not matches_to_remove or matches_left < matches_to_remove:
            user_input = self._get_verified_user_input(
                "Number of matches to remove (1-3): ", ['1', '2', '3'])
            matches_to_remove = int(user_input)

        self._output_to_screen('')
        return matches_to_remove


class ComputerPlayer(Player):
    def __init__(self, player_name, difficulty):
        self._difficulty = difficulty
        Player.__init__(self, "computer", player_name)

    def get_difficulty(self):
        return self._difficulty

    def play_round(self, matches_left):
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
