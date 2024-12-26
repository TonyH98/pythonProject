import skills


class swordStrike(skills):
    def __init__(self, strength: int, mp: int, type: str, accuracy: float, job: str):
        super().__init__(strength, mp, type, accuracy, job)

    def skillUse(self, playerAttack: int, monsterDefense: int) -> float:
        DAMAGE_MULTIPLIER = 1.8
        DEFENSE_REDUCTION = 2
        damage = ((playerAttack + self.strength) * DAMAGE_MULTIPLIER) - (monsterDefense - DEFENSE_REDUCTION)
        return max(0, damage)  # Ensure damage is not negative``~`  `