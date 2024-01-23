from human import Human
from kobold import Kobold

kobold1 = Kobold()
kobold2 = Kobold()
human1 = Human()

# combatants = [kobold1, kobold2]

# for idx, combatant in enumerate(combatants):
#     print(
#         f"The {idx + 1}. creature is a {combatant.__class__} with {combatant.get_current_hp()} hp"
#         f" and {combatant.damage} damage per round.")
#
# print()

# kobold1.hit(kobold2)
# kobold1.fight(kobold2)
kobold1.fight(human1)
