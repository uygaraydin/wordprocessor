import os
import sys
from PyQt5 import QtWidgets

class word_processor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.writefield=QtWidgets.QTextEdit()
        self.open=QtWidgets.QPushButton("Open")
        self.save=QtWidgets.QPushButton("Save")
        self.delete=QtWidgets.QPushButton("Delete")
        self.quit=QtWidgets.QPushButton("Quit")


        hb=QtWidgets.QHBoxLayout()
        hb.addWidget(self.open)
        hb.addWidget(self.save)
        hb.addWidget(self.delete)
        hb.addWidget(self.quit) 


        vb=QtWidgets.QVBoxLayout()
        vb.addWidget(self.writefield)

        vb.addLayout(hb)
        self.setLayout(vb)

        self.setWindowTitle("Word Processor App")

        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)
        self.delete.clicked.connect(self.delete_write)
        self.quit.clicked.connect(self.quit_app)

        self.show()


    def open_file(self):
            file=QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))

            with open(file[0],"r") as file:

                self.writefield.setText(file.read())

    def save_file(self):
            file=QtWidgets.QFileDialog.getSaveFileName(self,"Save File", os.getenv("Desktop"))

            with open(file[0], "w") as file:
                file.write(self.writefield.toPlainText())

    def delete_write(self):
            self.writefield.clear()

    def quit_app(self):
            quit()




object=QtWidgets.QApplication(sys.argv)

wordprocessor=word_processor()

sys.exit(object.exec())
