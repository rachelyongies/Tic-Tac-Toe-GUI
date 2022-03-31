import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from main_class import TicTacToe

qtCreatorFile = "ttt.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Main(QMainWindow, Ui_MainWindow):          
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons = {
            self.pushButton_1 : 1,
            self.pushButton_2 : 2,
            self.pushButton_3 : 3,
            self.pushButton_4 : 4,
            self.pushButton_5 : 5,
            self.pushButton_6 : 6,
            self.pushButton_7 : 7,
            self.pushButton_8 : 8,
            self.pushButton_9 : 9
        }
        for b in self.buttons:
            b.clicked.connect(self.PB_C)
        self.pushButton_reset.clicked.connect(self.PB_Reset) #like restart/reset the game
        self.lineEdit_choice.textChanged.connect(self.update_choice)
        self.players = { self.lineEdit_player1: 1, self.lineEdit_player2: 2 }
        self.lineEdit_player1.textChanged.connect(self.update_name)
        self.lineEdit_player2.textChanged.connect(self.update_name)

        self.o = TicTacToe("A", "B")
        self.o.players[1]["choice"] = self.lineEdit_choice.text()
        if self.lineEdit_choice.text() == "O":
            self.o.players[2]["choice"] = "X"
        else:
            self.o.players[2]["choice"] = "O"
        
        self.lineEdit_player1.setText("A")
        self.lineEdit_player2.setText("B")

    def PB_C(self):
        button = self.sender()
        move = self.buttons[button]
       
        if self.o.values[move-1] != ' ':
            message = "Place already filled. Try again!!"
            self.label_message.setText(message)
        self.o.values[move-1] = self.o.players[self.o.cur_player]["choice"]
        self.o.players[self.o.cur_player]["pos"].append(move)
        self.display_board()
        if self.o.check_win():
            print("hello")
            message = "Player "+ self.o.players[self.o.cur_player]["name"]+ " has won the game!!"
            self.label_message.setText(message)
            #disactivate all buttons
        if self.o.check_draw():
            message = "Game Drawn"
            self.label_message.setText(message)
        self.o.change_cur_player()


    def PB_Reset(self):
        self.o.players[1]["pos"] = []
        self.o.players[2]["pos"] = []
        self.o.values = [' ' for x in range(9)]
        self.display_board()

        self.o.players[1]["choice"] = self.lineEdit_choice.text()
        if self.lineEdit_choice.text() == "O":
            self.o.players[2]["choice"] = "X"
        else:
            self.o.players[2]["choice"] = "O"
        
        self.o.cur_player = self.o.start_player
    
    def display_board(self):
        for b,v in self.buttons.items():
            b.setText(self.o.values[v-1]) #b is the btn, v is 1, v-1 is the index for values list
   
    def update_choice(self):
        self.o.players[1]["choice"] = self.lineEdit_choice.text()
        if self.lineEdit_choice.text() == "O":
            self.o.players[2]["choice"] = "X"
        else:
            self.o.players[2]["choice"] = "O"
    def update_name1(self):
        self.o.players[1]["name"] = self.lineEdit_player1.text()
    def update_name2(self):
        self.o.players[2]["name"] = self.lineEdit_player2.text()
    def update_name(self):
        line = self.sender()
        self.o.players[self.players[line]]["name"] = line.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())