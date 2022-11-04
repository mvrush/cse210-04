# This is the scoring class programmed by -Matt Rushton-
from game.casting.actor import Actor

class Scoring:
    
    def __init__(self):
        self.actor = Actor() # This creates an instance (instantiates) of our Actor() class giving us access to it's methods and public variable (I don't think the private ones)
        self._total_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._total_score'. It holds our cumulative score
    
    def set_score(self):
        """
        if self.actor.get_text() == "*":
            self._total_score += 1
        elif self.actor.get_text() == "0":
            self._total_score -= 1
        """
        self._total_score += 100
        
        return self._total_score
    
    def get_score(self):

        return self._total_score

