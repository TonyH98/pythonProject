import monster 

class JazzVigalante(monster):

    def __init__(self, health, strength, defense, speed, intelligence, mp, skills, exp, money):
        super().__init__(health, strength, defense, speed, intelligence, mp, skills, exp, money)
    

    def vigalanteAI(self, player):
        if(player.health < player.health / 2):
            self.defense 
