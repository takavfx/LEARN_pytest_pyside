import sys
from PySide2 import QtCore
from PySide2 import QtWidgets


class SampleDialog(QtWidgets.QDialog):

    def __init__(self, *args):
        super(SampleDialog, self).__init__(*args)
        
        self.number = 0

        self.setWindowTitle('Hello, World!')
        self.resize(300, 200)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(str(self.number))

        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Add Count')
        self.button.clicked.connect(self.add_count)
        self.button.setMinimumSize(200, 100)

        layout.addWidget(self.button)

        self.setLayout(layout)
        self.resize(200, 100)


    def add_count(self):
        self.number += 1
        self.label.setText(str(self.number))


def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    gui = SampleDialog()
    gui.show()
    
    app.exec_()
    

if __name__ == '__main__':
    main()
    