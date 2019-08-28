from player import Player
from match_pile import MatchPile
from cycling_iterator import CyclingIterator


class Game:
    def __init__(self, player_configs, pile_config):
        self._match_pile = MatchPile(pile_config)
        self._players = []
        for player_config in player_configs:
            self._players.append(Player.create(player_config,
                                               self._match_pile))
        self._active_player = None
        self._player_selector = CyclingIterator(self._players)
        self._turn = 0

    def get_turn(self):
        return self._turn

    def play(self):
        while self._match_pile.get_remaining_matches():
            self._output_to_screen("There's a pile of matches on the table:"
                                   "\n")
            self._match_pile.draw_matches()
            self._turn += 1
            self._active_player = self._player_selector.advance()
            self._get_user_input("Press <Enter> for "
                                 + self._active_player.get_name()
                                 + "'s turn.\n")
            self._active_player.play_turn()

        self._output_to_screen(self._active_player.get_name() + ' loses!\n')

    def _output_to_screen(self, output):
        print(output)

    def _get_user_input(self, query_text):
        return input(query_text)
