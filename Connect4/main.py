import tkinter as tk
from tkinter import messagebox

class ConnectFourGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = []
        for row in range(6):
            button_row = []
            for col in range(7):
                button = tk.Button(self.master, text=' ', width=8, height=4,
                                   font=('Arial', 14), padx=10, pady=10,
                                   command=lambda row=row, col=col: self.drop_token(row, col))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
        
    def drop_token(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(row, col):
                self.game_over()
            elif all(self.board[row][col] != ' ' for col in range(7) for row in range(6)):
                self.tie_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def check_win(self, row, col):
        token = self.board[row][col]
        # Check rows
        if any(all(self.board[row][col+i] == token for i in range(4)) for col in range(4) for row in range(6)):
            return True
        # Check columns
        if any(all(self.board[row+i][col] == token for i in range(4)) for col in range(7) for row in range(3)):
            return True
        # Check diagonals
        if any(all(self.board[row+i][col+i] == token for i in range(4)) for col in range(4) for row in range(3)):
            return True
        if any(all(self.board[row+i][col+3-i] == token for i in range(4)) for col in range(4) for row in range(3)):
            return True
        return False
    
    def game_over(self):
        winner = self.current_player
        self.current_player = None
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.ask_restart_game()
        
    def tie_game(self):
        tk.messagebox.showinfo("Game Over", "It's a tie!")
        self.ask_restart_game()
        
    def ask_restart_game(self):
        answer = tk.messagebox.askquestion("Restart Game", "Do you want to restart the game?")
        if answer == 'yes':
            self.reset_game()
        else:
            self.master.destroy()
        
    def reset_game(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        for row in range(6):
            for col in range(7):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()
