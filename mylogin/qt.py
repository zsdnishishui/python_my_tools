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
        self.resize(400,100)
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        username, password = get_save()
        reviewEdit = QTextEdit()
        reviewEdit.setReadOnly(True)
        grid = QGridLayout()
        grid.setSpacing(2)
        if username == '' or password == '':
            username_label = QLabel('用户名')
            password_label = QLabel('密码')
            usernameEdit = QLineEdit()
            passwordEdit = QLineEdit()
            passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
            btn = QPushButton('登陆', self)
            btn2 = QPushButton('隐藏', self)
            grid.addWidget(username_label, 1, 0)
            grid.addWidget(usernameEdit, 1, 1)

            grid.addWidget(password_label, 2, 0)
            grid.addWidget(passwordEdit, 2, 1)

            grid.addWidget(btn, 3, 0)
            grid.addWidget(btn2, 2, 2)
            btn.clicked.connect(lambda: self.clickButton(usernameEdit.text(), passwordEdit.text(), True, reviewEdit))
            btn2.clicked.connect(lambda: self.clickButton2(btn2,passwordEdit))
        else:
            self.clickButton(username, password, False, reviewEdit)

        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.center()
        self.setWindowTitle('自动登陆')
        self.show()

    def clickButton(self, username, password, encryption, reviewEdit=None):
        if username == '' or password == '':
            reviewEdit.setText("用户名密码不能为空！")
            return
        res = login(username, password, encryption)
        reviewEdit.setText(res)

    def clickButton2(self,btn2,passwordEdit):
        if btn2.text() == '显示':
            btn2.setText('隐藏')
            passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            btn2.setText('显示')
            passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
