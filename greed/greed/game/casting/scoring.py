# This is the scoring class programmed by -Matt Rushton-
# from game.casting.cast import Cast # Don't need this since we are catching the instance of 'class' from directory.py that was instantiated in __main__.py

class Scoring:
    
    def __init__(self):
        #self._cast = Cast() # Don't need this anymore This creates an instance (instantiates) of our Cast() class giving us access to it's methods and public variables (I don't think the private ones)
        self._total_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._total_score'. It holds our cumulative score
    
    def set_score(self, cast): # recieves the 'cast' instance from the call in 'director.py' which is actually an instance of our 'Cast()' class instantiaed in __main__.py
        #self._total_score += 100 # This line for testing only

        actors = cast.get_actors("artifacts") #  __main__.py runs first and uses an instance of the 'Cast()' class called 'class' That's where it's populated. This passes the 'artifacts' key to 'get_actors()' in the 'cast' insance of 'Cast()' class
        #print(actors) # prints all of the objects in the cast which if pulls from the 'director.py' from an instance of 'Cast()' found in __main__.py
        for actor in actors:
            print(actor) # Prints the object but can't get the data.
            if actor == "*":
                self._total_score += 1
            elif actor == "0":
                self._total_score -= 1
        
        return self._total_score
    
    def get_score(self):

        return self._total_score

