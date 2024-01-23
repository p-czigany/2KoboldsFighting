import time


class Combatant:
    def __init__(self):
        self.damage = None
        self.current_hp = None

    def is_alive(self):
        return self.current_hp > 0

    def get_current_hp(self):
        return self.current_hp

    def suffer_harm(self, how_much):
        print(f"{self} suffers {how_much} damage")
        self.current_hp -= how_much

    def hit(self, other):
        print(f"{self} hits {other} for {self.damage} damage")
        other.suffer_harm(self.damage)
        time.sleep(1)

    def fight(self, other):
        print(f"{self} and {other} are fighting each other for their lives")
        time.sleep(2)
        round_index = 0
        while self.is_alive() and other.is_alive():
            round_index += 1
            print(f"Round #{round_index} begins:")
            time.sleep(1)
            self.hit(other)
            other.hit(self)
        print(f"The fight is over. It took {round_index} rounds.")
        if self.is_alive():
            print(f"{self} won the fight")
        elif other.is_alive():
            print(f"{other} won the fight")
        else:
            print(f"Both {self} and {other} are dead.")
