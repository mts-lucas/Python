from rpg_pybot.players.player import Player

from rpg_pybot.dice.roll import roll

print("Jogando 3 d6")
roll(3, 6)

lucas = Player("Lucas")
samuca = Player("Samuca")

lucas.set_char_class(0)
samuca.set_char_class(3)

lucas.player_data()
print()
samuca.player_data()

lucas.attack(samuca)
print()
samuca.attack(lucas)
print()
lucas.player_data()
print()
samuca.player_data()

