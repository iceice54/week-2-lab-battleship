class Board:
    def __init__(self):
        self.placement = [([0] * 10)] * 10
        self.hit = [([0] * 10)] * 10
        self.placeShip("carrier")
        self.placeShip("submarine")
    
    def placeShip(self, ship):
        if ship == "carrier":
            shipLength = 4
        elif ship == "submarine":
            shipLength = 3

        try:
            orientation, row, column = input("Enter info: \"orientation,row,column\": ").split(",")
        except:
            raise
        
        if orientation == "h":
            print(type(row))
            for i in self.placement[int(row)]:
                print("hi")
        elif orientation == "v":
            print("hello world")
        else:
            raise ValueError("invalid orientation")

        print(orientation)
        print(row)
        print(column)
        print(shipLength)

def printBoard(board):
    for i in board:
        print (i)

p1Board = Board()
# printBoard(p1Board.placement)
