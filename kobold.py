from combatant import Combatant


class Kobold(Combatant):
    def __init__(self):
        super().__init__()
        self.current_hp = 6
        self.damage = 2
