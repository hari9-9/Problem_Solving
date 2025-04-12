class Player:
    def __init__(self , name : str , symbol : str):
        self.name = name
        self.symbol = symbol


class Move:
    def __init__(self , symbol : str , row :int , col : int):
        self.symbol = symbol
        self.row = row
        self.col = col


class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        pass
    
    def update_board(self ,move : Move) -> bool:
        if self.grid[move.row][move.col] == '':
            self.grid[move.row][move.col] = move.symbol
            return True
        return False
    
    def is_full(self):
        pass
    
    def check_win(self , symbol):
        pass


class TicTacToe:
    def __init__(self , player1 : Player , player2 : Player):
        self.board = Board()
        self.players = [player1 , player2]
        self.curr_turn = 0
    
    def switch_turn(self):
        if self.curr_turn:
            self.curr_turn = 0
        else:
            self.curr_turn = 1
    
    def get_move(self):
        row = input()
        col = input()
        player = self.players[self.curr_turn]
        return Move(player.symbol , row , col)
    
    
    def play_move(self):
        move = self.get_move()
        self.board.update_board(move)
    
    def play_game(self):
        win = False
        while not win and not self.board.is_full():
            self.board.print_board()
            move = self.get_move()
            if not self.board.update_board(move):
                print("Invalid move, cell already taken. Try again.")
                continue  # Skip switching turn if move was invalid
            
            if self.board.check_win(self.players[self.curr_turn].symbol):
                self.board.print_board()
                print(f"{self.players[self.curr_turn].name} wins!")
                win = True
                break
            
            if self.board.is_full():
                self.board.print_board()
                print("It's a draw!")
                break
            
        self.switch_turn()
        
    