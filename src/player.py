# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, location, backpack=[]):
        self.name = name
        self.location = location
        self.backpack = backpack

    def myItems(self):
        for i in self.backpack:
            print(i)

    def grabItem(self, item):
        return self.backpack.append(item)

    def dropItem(self, item):
        return self.backpack.remove(item)