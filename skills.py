class Skills:
    def __init__(self, strength: int, mp: int, type: str, accuracy: float, job: str):
        self.strength = strength
        self.mp = mp
        self.type = type
        self.accuracy = accuracy
        self.job = job

    def skillUse(self, playerAttack: int, monsterDefense: int) -> float:
        DAMAGE_MULTIPLIER = 1.5
        damage = ((playerAttack + self.strength) * DAMAGE_MULTIPLIER) - monsterDefense
        return max(0, damage)  # Ensure damage is not negative
