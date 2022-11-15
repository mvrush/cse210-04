import random
from game.casting.artifact import Artifact
from game.shared.point import Point # Had to import this so I could use Point() class to set velocity for the artifacts.
from game.shared.color import Color # Had to import to regenerate artifacts         
            
                
### To regenerate artifacts I need these variable values
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60 # This splits the width (x) into 60 columns
ROWS = 40 # This splits the height (y) into 40 rows


class Gem(Artifact):

    def __init__(self):
        super().__init__() # Using 'super()' and dot . notation invokes the Parent constructor from the Actor() class. Basically calls the Actor() class '__init__(self)' constructor and gives you access to all it's attributes. 
        self._text = '*'

    def add_remove_artifact(self, cast): # Receives the instance of 'cast' created in __main__.py from the call to 'add_remove_gem()' in director.py

        # cast = Cast() # Creates an instance of Cast()

        ### Add new artifact when the robot position and artifact position are the same (replaces the removed ones)
        # I just took the following lines right out of the CREATE ARTIFACT section of the __main__.py file
        #text = random.choice(['*', '0']) # This line uses the random.choice() function to choose between the string '*' or '0' {zero}.
        text = self._text

        x = random.randint(1, COLS - 1) # This sets a random value for our x (horizontal) position in the columns
        y = random.randint(1, ROWS - 1) # This sets a random value for our y (vertical) position in the rows
        position = Point(x, y) # this will be the position for one artifact as it loopws.
        position = position.scale(CELL_SIZE) # sets the position size to equal what we defined for our CELL_SIZE

        # The next 4 lines create a random color for each artifact
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # Calls our Artifact() class and sets each of the values below using the methods in the Artifact() class
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        #artifact.set_message(message) # We don't need a message anymore.
        cast.add_actor("artifacts", artifact) # problem is, it can't access the instantiation of 'cast' in the __main__.py