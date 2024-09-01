class Board:
    def __init__(self, player):
        self.placement = [[0 for i in range(10)] for k in range(10)]
        self.hit = [[0 for i in range(10)] for k in range(10)]
        self.placeShip("carrier", player)
        self.placeShip("submarine", player)
    
    def placeShip(self, ship, player):
        if ship == "carrier":
            shipLength = 4
        elif ship == "submarine":
            shipLength = 3

        try:
            orientation, row, column = input(f"{player} where do you want to place your {ship}? Enter in this format: \"orientation,row,column\": ").split(",")
        except:
            raise
        
        if orientation == "h":
            for columnNum in range(ord(column)-97, ord(column) - 97 + shipLength):
                if self.placement[int(row)-1][columnNum] == 1:
                    raise IndexError("Your ships are overlapping!")
                self.placement[int(row)-1][columnNum] = 1
        elif orientation == "v":
            for rowNum in range(int(row), int(row) + shipLength):
                if self.placement[rowNum-1][ord(column)-97] == 1:
                    raise IndexError("Your ships are overlapping!")
                self.placement[rowNum-1][ord(column)-97] = 1
        else:
            raise ValueError("invalid orientation")
        
        self.printBoard()
        
        # self.printBoard()

        # print(orientation)
        # print(row)
        # print(column)
        # print(shipLength)

    def printBoard(self):
        for i in self.placement:
            print(i)

class Game:
    def __init__(self):
        p1Board = Board("Player 1")
        p2Board = Board("Player 2")
        p1points = 0
        p2points = 0
        while (p1points < 7 or p2points < 7):
            p1points += self.takeTurn(p2Board, "Player 1")
            p2points += self.takeTurn(p1Board, "Player 2")

    def takeTurn(self, board:Board, player):
        row, column = input(f"{player}, what row and column do you want to attack?").split(",")
        print(f"Attacking row {row} and column {column}")
        target = board.placement[int(row)-1][ord(column)-97]
        if target == 1:
            #Attack hits target
            print("You hit a ship!")
            board.placement[int(row)-1][ord(column)-97] = "X"
            board.printBoard()
            return 1
        elif target == 0:
            print("You missed!")
            board.printBoard()
            return 0
        elif target == "X":
            print("You have already hit a ship there")
            board.printBoard()
            return 0

game = Game()
# printBoard(p1Board.placement)
