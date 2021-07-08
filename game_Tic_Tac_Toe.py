import tkinter as Tkinter

class Game(Tkinter.Tk):
    def __init__(self,master):
        self.master = master
        Tkinter.Tk.__init__(self,master)
        self.player = 1
        self.lst = [[0,0,0],[0,0,0],[0,0,0]]
        self.nr = 1
        self.start_game()    


    def start_game(self):
        self.grid()
        self.player = 1
        for row in range(8):
            self.grid_rowconfigure(row, minsize=30)
            
        self.label =  Tkinter.Label(self.master, text='', height = 2, width = 10)
        self.label.grid(row=4)
        
        self.button1 =  Tkinter.Button(self.master, text='', command = lambda: self.check_game(1), height = 2, width = 5)
        self.button1.grid(row=1, column=2)
        
        self.button2 =  Tkinter.Button(self.master, text='', command = lambda: self.check_game(2), height = 2, width = 5)
        self.button2.grid(row=1, column=3)
        
        self.button3 = Tkinter.Button(self.master, text='', command = lambda: self.check_game(3), height = 2, width = 5)
        self.button3.grid(row=1, column=4)
        
        self.button4 =  Tkinter.Button(self.master, text='', command = lambda:self.check_game(4), height = 2, width = 5)
        self.button4.grid(row=2, column=2)
        
        self.button5 =  Tkinter.Button(self.master, text='', command = lambda: self.check_game(5), height = 2, width = 5)
        self.button5.grid(row=2, column=3)
        
        self.button6 =  Tkinter.Button(self.master, text='', command = lambda:self.check_game(6), height = 2, width = 5)
        self.button6.grid(row=2, column=4)
        
        self.button7 =  Tkinter.Button(self.master, text='', command = lambda: self.check_game(7), height = 2, width = 5)
        self.button7.grid(row=3, column=2)
        
        self.button8 =  Tkinter.Button(self.master, text='', command = lambda:self.check_game(8), height = 2, width = 5)
        self.button8.grid(row=3, column=3)
        
        self.button9 =  Tkinter.Button(self.master, text='', command = lambda: self.check_game(9), height = 2, width = 5)
        self.button9.grid(row=3, column=4)

        self.button10 =  Tkinter.Button(self.master, text='START \nAGAIN', command = self.start_game_again, height = 2, width = 5)
        self.button10.grid(row=6, column=2)
        
        self.button11 =  Tkinter.Button(self.master, text='EXIT \nGAME', command = self.exit_game, height = 2, width = 5)
        self.button11.grid(row=6, column=4)

    def show_status_game(self):      
        y = self.compute_sums()
        if y == 1:
            self.label.config(text='X won')
            return 1
        elif y == 2:
            self.label.config(text='O won')
            return 2
        elif y !=1 or y!= 2:
            if self.nr == 10:
                self.label.config(text='Nobody won')
            return 3
        
    def stop_game(self):
        y = self.show_status_game()
        if y == 1 or y == 2 or self.nr == 10:
            self.button1.config(state="disable")
            self.button2.config(state="disable")
            self.button3.config(state="disable")
            self.button4.config(state="disable")
            self.button5.config(state="disable")
            self.button6.config(state="disable")
            self.button7.config(state="disable")
            self.button8.config(state="disable")
            self.button9.config(state="disable")
            return True
        else:
            return False
            
    def switch_player(self):
        self.nr += 1
        if self.player == 1:
            self.player = 10
            self.label.config(text='Now is 0')
            self.label.grid(row = 4)
        else:
            self.player = 1
            self.label.config(text='Now is x')
            self.label.grid(row = 4)
        
    def start_game_again(self):
        self.destroy()
        app = main()
        
    def exit_game(self):
        self.destroy()
        
    def update_button_text(self):
        if self.player == 1:
            return "X"
        else:
            return "0"
    
    def check_game(self, button_id):
        if button_id == 1:
            self.lst[0][0] = self.player
            self.button1.config(state="disable")
            self.button1.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 2:
            self.lst[0][1] = self.player
            self.button2.config(state="disable")
            self.button2.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 3:
            self.lst[0][2] = self.player
            self.button3.config(state="disable")
            self.button3.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 4:
            self.lst[1][0] = self.player
            self.button4.config(state="disable")
            self.button4.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 5:
            self.lst[1][1] = self.player
            self.button5.config(state="disable")
            self.button5.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 6:
            self.lst[1][2] = self.player
            self.button6.config(state="disable")
            self.button6.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 7:
            self.lst[2][0] = self.player
            self.button7.config(state="disable")
            self.button7.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 8:
            self.lst[2][1] = self.player
            self.button8.config(state="disable")
            self.button8.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        elif button_id == 9:
            self.lst[2][2] = self.player
            self.button9.config(state="disable")
            self.button9.config(text = self.update_button_text())
            self.switch_player()
            self.show_status_game()
            
        x = self.compute_sums()
        if x == 1:
            self.stop_game()
        elif x == 2:
            self.stop_game()
        elif x == 0:
            self.stop_game()
        else: 
            pass
        
    def compute_sums(self):
        s0 = self.compute_sum0(self.lst)
        s1 = self.compute_sum1(self.lst)
        s2 = self.compute_sum2(self.lst)
        s3 = self.compute_sum3(self.lst)
        s4 = self.compute_sum4(self.lst)
        s5 = self.compute_sum5(self.lst)
        s6 = self.compute_sum_diag_princ(self.lst)
        s7 = self.compute_sum_diag_sec(self.lst)
        return self.check_winner(s0,s1,s2,s3,s4,s5,s6,s7)
    
    def check_winner(self,s0,s1,s2,s3,s4,s5,s6,s7):
        if s0 == 3 or s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3 or s5 == 3 or s6 == 3 or s7 == 3:
            return 1
        elif s0 == 30 or s1 == 30 or s2 == 30 or s3 == 30 or s4 == 30 or s5 == 30 or s6 == 30 or s7 ==30:
            return 2
        elif self.nr == 9:
            return 0
        else:
            return 3
        
    def compute_sum_diag_princ(self,lst):
        s6 = self.lst[0][0] + self.lst[1][1] + self.lst[2][2] 
        return s6
    
    def compute_sum_diag_sec(self,lst):
        s7 = self.lst[2][0] + self.lst[1][1] + self.lst[0][2] 
        return s7
    
    def compute_sum0(self,lst):
        s0 = 0
        for i in range(3):
            s0 += self.lst[i][0]
        return s0
    
    def compute_sum1(self,lst):
        s1= 0
        for i in range(3):
            s1 += self.lst[i][1]
        return s1

    
    def compute_sum2(self,lst):  
        s2 = 0
        for i in range(3):
            s2 += self.lst[i][2]
        return s2
    
    def compute_sum3(self,lst):
        s3 = 0
        for i in range(3):
            s3 += self.lst[0][i]
        return s3
    
    def compute_sum4(self,lst):
        s4 = 0
        for i in range(3):
            s4 += self.lst[1][i]
        return s4
    
    def compute_sum5(self,lst):
        s5 = 0
        for i in range(3):
            s5 += self.lst[2][i]
        return s5
    
def main():
    app = Game(None)
    app.title("Tic Tac Toe")
    app.geometry("300x300")
    app.mainloop()
    
if __name__ == "__main__":
    main()
