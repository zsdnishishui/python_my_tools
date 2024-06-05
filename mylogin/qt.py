import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QMessageBox)
from login import login, get_save


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.loginUI()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        self.resize(300,100)
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def loginUI(self):
        username, password = get_save()
        if username == '' or password == '':
            self.initUI()
        else:
            self.clickButton(username, password, False)
            self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        username_label = QLabel('输入用户名')
        password_label = QLabel('输入密码')
        usernameEdit = QLineEdit()
        passwordEdit = QLineEdit()
        passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        btn = QPushButton('登陆', self)
        btn2 = QPushButton('显示密码', self)
        grid.addWidget(username_label, 1, 0)
        grid.addWidget(usernameEdit, 1, 1)

        grid.addWidget(password_label, 2, 0)
        grid.addWidget(passwordEdit, 2, 1)

        grid.addWidget(btn2, 3, 0)
        grid.addWidget(btn, 3, 1)
        btn.clicked.connect(lambda: self.clickButton(usernameEdit.text(), passwordEdit.text(), True))
        btn2.clicked.connect(lambda: self.clickButton2(btn2,passwordEdit))
        self.setLayout(grid)
        self.center()
        self.setWindowTitle('自动登陆')
        self.show()




    def clickButton(self, username, password, encryption):
        if username == '' or password == '':
            QMessageBox.information(self,"提示","用户名密码不能为空！")
            return
        res = login(username, password, encryption)
        QMessageBox.about(self,"提示",res)
        if res == '登陆成功':
            sys.exit()
        return res

    def clickButton2(self,btn2,passwordEdit):
        if btn2.text() == '显示密码':
            btn2.setText('隐藏密码')
            passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            btn2.setText('显示密码')
            passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
