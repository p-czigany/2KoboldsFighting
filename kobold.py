HP = 6
DAMAGE = 2


class Kobold(object):
    def __init__(self):
        super().__init__()
        self.max_hp = HP
        self.current_hp = HP
        self.damage = DAMAGE
        self.is_alive = True

    def get_current_hp(self):
        if not self.is_alive:
            print(f"{self} is already dead")
        return self.current_hp

    def suffer_harm(self, how_much):
        if self.is_alive:
            print(f"{self} suffers {how_much} damage")
            self.current_hp -= how_much
            if self.current_hp <= 0:
                print(f"{self} dies")
                self.current_hp = 0
                self.is_alive = False
        else:
            print(f"{self} is already dead, can't suffer more harm")

    def hit(self, other):
        if self.is_alive:
            print(f"{self} hits {other} for {self.damage} damage")
            other.suffer_harm(self.damage)
        else:
            print(f"{self} is dead, can't hit anybody")
