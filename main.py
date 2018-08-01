from game import Game

pile_config = {'number_of_matches': 9, 'type': 'triangle'}

player_2_config = {'type': 'computer', 'name': 'Computer',
                   'difficulty': 'hard'}
player_1_config = {'type': 'human', 'name': 'Man'}
player_configs = [player_1_config, player_2_config]

game = Game(player_configs, pile_config)

game.play()
