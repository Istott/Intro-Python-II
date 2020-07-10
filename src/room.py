# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name}{self.description}'

    def itemList(self):
        for i in self.items:
            print(f'{i}')

    def removeRoomItem(self, item):
        return self.items.remove(item)
    
    def addRoomItem(self, item):
        return self.items.append(item)

        
