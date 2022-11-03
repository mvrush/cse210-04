from game.casting.actor import Actor


class Artifact(Actor): # Creates the Artifact() class and gets inheritance from the Actor class. That gives it access to all the Actor() class attributes and methods that aren't private.
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__() # Using 'super()' and dot . notation invokes the Parent constructor from the Actor() class. Basically calls the Actor() class '__init__(self)' constructor and gives you access to all it's attributes.
        self._message = "" # This adds another Attribute found only in our Artifact() class called 'self._message'
        
    def get_message(self): # This function passes the value of 'self._message' out. Basically gives it public access. It's a getter function.
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message): # This function sets the value of 'self._message' by taking a value for 'message' from whatever calls the function and passes a message value. Basically gives it public access. It's a setter function.
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message