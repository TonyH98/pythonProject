
class Skills:
    
    def __init__(self, strength, mp, type, accuracy, job):
        self.strength = strength
        self.mp = mp
        self.type = type
        self.accuracy = accuracy
        self.job = job
    
    def skillUse(self, playerAttack, monsterDefense):
        #Atk*1.5 - Def
        damage = ((playerAttack + self.strength) * 1.5) - monsterDefense

        return damage 
