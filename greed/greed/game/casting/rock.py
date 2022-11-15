from game.casting.gem import Gem

class Rock(Gem):

    def __init__(self):
        super().__init__() # Using 'super()' and dot . notation invokes the Parent constructor from the Actor() class. Basically calls the Actor() class '__init__(self)' constructor and gives you access to all it's attributes. 
        self._text = '0'