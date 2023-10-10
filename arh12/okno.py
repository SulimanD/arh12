import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QMessageBox,QLabel,QLineEdit,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt

### список зарегистрированных пользователей
list = {'Anton': 458,'Pavel': 474}

class MessengerWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        ### цвет фона окна
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.cyan)
        self.setPalette(palette)

        ### поля для ввода логина и пароля
        self.okno_login = QLineEdit(self)
        self.okno_login.move(80, 40)

        self.okno_password = QLineEdit(self)
        self.okno_password.move(80, 70)

        ### подписи к полям ввода логина и пароля
        self.lbl = QLabel('login:', self)
        self.lbl.move(52, 40)
        
        self.lbl_1 = QLabel('password:', self)
        self.lbl_1.move(29, 70)

        ### кнопки
        btn = QPushButton('LOG IN', self)
        btn.resize(btn.sizeHint())
        btn.move(110, 120)
        btn.clicked.connect(self.logIn)

        btn1 = QPushButton('SIGN UP', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(110, 150)
        btn1.clicked.connect(self.signUp)

        ### расположение и заголовок окна
        self.setGeometry(550, 300, 300, 200)
        self.setWindowTitle('Messenger')
        self.show()

    def logIn(self):  ### функция, которая будет выполняться после нажатия кнопки btn (LOG IN)
        a = self.okno_login.text() ### текст из поля login
        b = self.okno_password.text() ### текст из поля password
        print('вы зашли в систему под логином ', a)

    def signUp(self):  ### функция, которая будет выполняться после нажатия кнопки btn1 (SIGN IN)
        аа = self.okno_login.text() ### текст из поля login
        bb = self.okno_password.text() ### текст из поля password
        print('вы зарегистрированы под логином ', аа)

    def closeEvent(self, event):    ### функция предупреждения о выходе

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MessengerWindow()
    sys.exit(app.exec_())