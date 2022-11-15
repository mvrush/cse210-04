from game.casting.scoring import Scoring
from game.shared.point import Point # Had to import this so I could use Point() class to set velocity for the artifacts.
from game.casting.gem import Gem # imports the Gem class so I can use it during regeneration and deletion
from game.casting.rock import Rock # imports the Gem class so I can use it during regeneration and deletion


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
        self._gem = Gem()
        self._rock = Rock()
        
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
                
                ### the following is a loop within the loop to replace the removed rock or gem.
                if artifact.get_text() == "*": # looks at the value of the text for each artifact in loop
                    self._gem.add_remove_artifact(cast) # this will add an '*'
                else:
                    self._rock.add_remove_artifact(cast) # this will add an '0'
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()