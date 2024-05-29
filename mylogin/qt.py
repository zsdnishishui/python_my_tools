
import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton)
from login import login

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def initUI(self):

        title = QLabel('用户名：')
        author = QLabel('密码：')
        btn = QPushButton('登陆', self)

        # btn.clicked.connect(None)
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(btn, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        btn.clicked.connect(lambda: self.clickButton(titleEdit.text(), authorEdit.text(),reviewEdit))
        self.setLayout(grid)

        self.center()
        self.setWindowTitle('自动登陆')
        self.show()
    def clickButton(self, username, password, reviewEdit=None):
        res = login(username, password)
        reviewEdit.setText(res)

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()