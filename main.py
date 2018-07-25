from match_pile import MatchPile
from player import ComputerPlayer
from player import HumanPlayer

pile = MatchPile(4, "triangle")

print(pile.get_remaining_matches())
player1 = HumanPlayer("Jokamies", pile)
player2 = ComputerPlayer("Machine", "Hard", pile)
players = [player1, player2]
players[0].play_turn()
print(pile.get_remaining_matches())
# players.append(player1)
# players.append(player2)
# print(players[0]._name)
# print(players[0]._type)
# print(players[1]._name)
# print(players[1]._type)
# print(players[1]._difficulty)

# print (player2._determine_randomness("hard"))
# print (player2._choose_matches(4, True))

# num = player1.convert_to_int("2")
# print(num)
# player1._choose_matches()