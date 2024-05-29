import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton)
from login import login, get_save


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
        username, password = get_save()
        reviewEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        if username == '' or password == '':
            title = QLabel('用户名：')
            author = QLabel('密码：')
            titleEdit = QLineEdit()
            authorEdit = QLineEdit()
            btn = QPushButton('登陆', self)
            grid.addWidget(title, 1, 0)
            grid.addWidget(titleEdit, 1, 1)

            grid.addWidget(author, 2, 0)
            grid.addWidget(authorEdit, 2, 1)

            grid.addWidget(btn, 3, 0)
            btn.clicked.connect(lambda: self.clickButton(titleEdit.text(), authorEdit.text(), True, reviewEdit))
        else:
            self.clickButton(username, password, False, reviewEdit)

        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.center()
        self.setWindowTitle('自动登陆')
        self.show()

    def clickButton(self, username, password, encryption, reviewEdit=None):
        res = login(username, password, encryption)
        reviewEdit.setText(res)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
