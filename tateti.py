class TaTeTi():

    def __init__(self, tablero=None):
        if not tablero:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = tablero

    def full(self):
        for j in range(9):
            if self.board[j] == " ":
                return False

        return True

    def fila(self):
        if self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x':
            return True
        if self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x':
            return True
        if self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x':
            return True
        if self.board[0] == 'o' and self.board[1] == 'o' and self.board[2] == 'o':
            return True
        if self.board[3] == 'o' and self.board[4] == 'o' and self.board[5] == 'o':
            return True
        if self.board[6] == 'o' and self.board[7] == 'o' and self.board[8] == 'o':
            return True
        
        return False
    
    def columna(self):
        if self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            return True
        if self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o':
            return True
        if self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            return True
        if self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o':
            return True
        if self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            return True
        if self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o':
            return True
        
        return False

    def diagonal(self):
        if self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            return True
        if self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o':
            return True
        if self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x':
            return True
        if self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o':
            return True
        
        return False

    def win(self):
        if self.fila() or self.columna() or self.diagonal():
            return True
        
        return False

    def validate(self, position):
        if self.board[position-1] == " ":
            return True

        return False

    def assign(self, position, piece):
        if self.validate(position) is False:
            raise Exception
        else:
            self.board[position - 1] = piece

    def draw_board(self):
        self.display = "\n"
        for num in range(9):
            if self.board[num] != " ":
                self.display += " " + self.board[num] + " "
            else:
                self.display += " " + str(1+num) + " "
            if num == 2 or num == 5:
                self.display += "\n---+---+---\n"
            elif num == 8:
                self.display += "\n"
            else:
                self.display += "|"

        return self.display
