# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, location):
        # super().__init__()
        self.name = name
        self.location = location
    
    # def try_direction(command):
    #     attribute = command + '_to'

    #     if hasattr(self.location, attribute):
    #         getattr(self.location, attribute)