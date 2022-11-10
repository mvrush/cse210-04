# This is the scoring class programmed by -Matt Rushton-
# from game.casting.cast import Cast # Don't need this since we are catching the instance of 'class' from directory.py that was instantiated in __main__.py

class Scoring:
    
    def __init__(self):
        #self._cast = Cast() # Don't need this anymore This creates an instance (instantiates) of our Cast() class giving us access to it's methods and public variables (I don't think the private ones)
        self._total_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._total_score'. It holds our cumulative score
    
    # New way of doing it where it just passes the 'text' value of the matched artifact
    def set_score(self, text):
        if text == "*":
            print("It was an astrisk")
            self._total_score += 1
        elif text == "0":
            print("It was a zero")
            self._total_score -= 1
        
        return self._total_score
    
    def get_score(self):

        return self._total_score

