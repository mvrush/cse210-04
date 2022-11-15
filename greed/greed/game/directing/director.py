import random # import the random library to use below

from game.casting.scoring import Scoring
from game.shared.point import Point # Had to import this so I could use Point() class to set velocity for the artifacts.
from game.shared.color import Color # Had to import to regenerate artifacts
from game.casting.artifact import Artifact # Had to import this so I could manipulate the Rocks and Gems when removing and adding them after they are caught.

### To regenerate artifacts I need these variable values
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60 # This splits the width (x) into 60 columns
ROWS = 40 # This splits the height (y) into 40 rows

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard service, video service and scoring.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._scoring = Scoring() # This intantiates an instance of the 'Scoring()' class so we can access it's methods and variables
        
    def start_game(self, cast): # This recieves the 'cast' instantiation from '__main__.py'. It's an instance of our 'Cast()' class that's been populated.
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors passed from __main__.py.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts") # Uses our instance of 'cast' passed from '__main__.py' and runs the 'get_actors()' function passing the 'artifact' key to get the artifacts.

        # the next three lines sets the velocity for each artifact
        velocity = Point(0, 5) # I was able to use the Point() class here because I imported it up above. 
        for artifact in artifacts:
            artifact.set_velocity(velocity)
        
        banner.set_text(f"Score: {self._scoring.get_score()}") # This is where we will set our "Score: " banner. I accessed the 'get_score()' method directly.
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # This sets the movement for our artifacts the same way we move the robot
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
        
        ### Remove hit artifacts create new Artifacts also control the scoring        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()): # Here, when the robot and artifact are in the same position, it runs the following lines.
                self._scoring.set_score(artifact.get_text()) # Passes the value of 'text' from the matched artifact to scoring. After running this function, the score is changed and reflected in our 'banner.set_text()' line above.
                cast.remove_actor("artifacts", artifact) # This removes the artiface when the robot and artifact intersect.
                
                ### Add new artifact when the robot position and artifact position are the same (replaces the removed ones)
                # I just took lines 103-125 right out of the CREATE ARTIFACT section of the __main__.py file
                text = random.choice(['*', '0']) # This line uses the random.choice() function to choose between the string '*' or '0' {zero}.
                #message = messages[n] # We won't be using messages anymore

                x = random.randint(1, COLS - 1) # This sets a random value for our x (horizontal) position in the columns
                y = random.randint(1, ROWS - 1) # This sets a random value for our y (vertical) position in the rows
                position = Point(x, y) # this will be the position for one artifact as it loopws.
                position = position.scale(CELL_SIZE) # sets the position size to equal what we defined for our CELL_SIZE

                # The next 4 lines create a random color for each artifact
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                
                # Calls our RockGem() class and sets each of the values below using the methods in the Artifact() class
                artifact = Artifact()
                artifact.set_text(text)
                artifact.set_font_size(FONT_SIZE)
                artifact.set_color(color)
                artifact.set_position(position)
                #artifact.set_message(message) # We don't need a message anymore.
                cast.add_actor("artifacts", artifact)
                
        ###
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()