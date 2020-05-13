# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # base class for players
    def __init__(self, name, current_room, itemArr=[]):
        self.name = name
        self.current_room = current_room
        self.itemArr = itemArr

    def showItems(self):
        if(len(self.itemArr) > 0):
            for i in self.itemArr:
                print(i)
        else:
            print("There are no items in the room")

    # methods for piccking up item
    def getItem(self, item):
        return self.itemArr.append(item)

    # method to remove items
    def dropItem(self, item):
        return self.itemArr.remove(item)

    def __str__(self):
        return f"name: {self.name}\ncurrent_room: {self.current_room}"
