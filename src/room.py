# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # base class for rooms
    def __init__(self, name, description, itemArr=[]):
        self.name = name
        self.description = description
        self.itemArr = itemArr

    def showItems(self):
        if(len(self.itemArr) > 0):
            for i in self.itemArr:
                print(i)
        else:
            print("There are no items in the room")

    def __repr__(self):
        return f"Room({self.name, self.description, self.itemArr})"
