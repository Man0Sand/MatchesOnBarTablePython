import unittest
from unittest.mock import MagicMock, call
from game import Game


class TestGame(unittest.TestCase):
    def test_player_1_computer_loses(self):
        pile_config = {'number_of_matches': 9, 'type': 'triangle'}
        player_1_config = {'type': 'computer', 'name': 'Machine 1',
                           'difficulty': 'hard'}
        player_2_config = {'type': 'computer', 'name': 'Machine 2',
                           'difficulty': 'hard'}
        player_configs = [player_1_config, player_2_config]
        game = Game(player_configs, pile_config)

        pile_mock = MagicMock()
        game._match_pile._output_to_screen = pile_mock

        game._output_to_screen = MagicMock()
        game._get_user_input = MagicMock()

        piles_expected = []
        piles_expected.append('  I I  \n I I I \nI I I I\n')
        piles_expected.append('    I  \n I I I \nI I I I\n')
        piles_expected.append('       \n     I \nI I I I\n')
        piles_expected.append('       \n       \nI I I I\n')
        piles_expected.append('       \n       \n      I\n')
        calls = []
        for pile_expected in piles_expected:
            calls.append(call(pile_expected))

        self.assertEqual(0, game.get_turn())
        game.play()
        self.assertEqual(5, game.get_turn())
        pile_mock.assert_has_calls(calls)
        self.assertEqual('Machine 1', game._active_player.get_name())

    def test_player_2_human_loses(self):
        pile_config = {'number_of_matches': 9, 'type': 'triangle'}
        player_1_config = {'type': 'computer', 'name': 'Machine 2',
                           'difficulty': 'hard'}
        player_2_config = {'type': 'human', 'name': 'Man'}
        player_configs = [player_1_config, player_2_config]
        game = Game(player_configs, pile_config)

        pile_mock = MagicMock()
        game._match_pile._output_to_screen = pile_mock

        game._output_to_screen = MagicMock()
        game._get_user_input = MagicMock()

        piles_expected = []
        piles_expected.append('  I I  \n I I I \nI I I I\n')
        piles_expected.append('    I  \n I I I \nI I I I\n')
        piles_expected.append('       \n I I I \nI I I I\n')
        piles_expected.append('       \n     I \nI I I I\n')
        piles_expected.append('       \n       \n    I I\n')
        piles_expected.append('       \n       \n      I\n')
        calls = []
        for pile_expected in piles_expected:
            calls.append(call(pile_expected))

        human_mock = MagicMock(side_effect=['1', '3', '1'])
        game._players[1]._get_user_input = human_mock
        game._players[1]._output_to_screen = MagicMock()

        self.assertEqual(0, game.get_turn())
        game.play()
        self.assertEqual(6, game.get_turn())
        pile_mock.assert_has_calls(calls)
        self.assertEqual('Man', game._active_player.get_name())


if __name__ == '__main__':
    unittest.main()
