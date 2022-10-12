from rpg_pybot.players.player import Player

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

