import base64
import rsa
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QPlainTextEdit,
                             QPushButton, QGridLayout, QLabel, QMessageBox)


def new_keys():
    """生成新的公钥私钥并保存在当前目录"""
    (pubkey, privkey) = rsa.newkeys(1024)
    with open('public.pem', 'wb') as f:
        f.write(pubkey.save_pkcs1())
    with open('private.pem', 'wb') as f:
        f.write(privkey.save_pkcs1())


def get_keys() -> (str, str):
    """读取当前目录的公钥私钥文件，返回"""
    with open('public.pem', 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    with open('private.pem', 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())

    return privkey, pubkey


class RSA(QWidget):

    def __init__(self):
        super(RSA, self).__init__()
        self.text = QPlainTextEdit()
        self.signature = QPlainTextEdit()
        self.result = QPlainTextEdit()
        self.init_ui()

    def init_ui(self):
        """init the window and show it"""
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        ok_button1 = QPushButton('公钥加密')
        ok_button2 = QPushButton('私钥解密')
        ok_button3 = QPushButton('私钥签名')
        ok_button4 = QPushButton('公钥验证')

        grid.addWidget(QLabel("明文密文输入："), 1, 1)
        grid.addWidget(self.text, 1, 2)
        grid.addWidget(QLabel("签名："), 2, 1)
        grid.addWidget(self.signature, 2, 2)

        grid.addWidget(ok_button1, 1, 5)
        grid.addWidget(ok_button2, 1, 6)
        grid.addWidget(ok_button3, 2, 5)
        grid.addWidget(ok_button4, 2, 6)

        grid.addWidget(QLabel("结果："), 1, 7)
        grid.addWidget(self.result, 1, 8)

        ok_button1.clicked.connect(self.button1_clicked)
        ok_button2.clicked.connect(self.button2_clicked)
        ok_button3.clicked.connect(self.button3_clicked)
        ok_button4.clicked.connect(self.button4_clicked)

        self.resize(500, 100)
        self.center()
        self.setWindowTitle('RSA')
        self.show()

    def center(self):
        """make window located center."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button1_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(rsa.encrypt)
            self.result.setPlainText(result)
        except ValueError:
            self.show_dialog()

    def button2_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(rsa.decrypt)
            self.result.setPlainText(result)
        except ValueError:
            self.show_dialog()

    def button3_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(rsa.sign)
            self.result.setPlainText(result)
        except ValueError:
            self.show_dialog()

    def button4_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(rsa.verify)
            self.result.setPlainText(result)
        except ValueError:
            self.show_dialog()

    def get_result(self, func):
        plain = self.text.toPlainText()
        signature = self.signature.toPlainText()
        privkey, pubkey = get_keys()
        func_name = func.__name__
        if func_name == 'encrypt':
            result = base64.b64encode(func(plain.encode(), pubkey)).decode()

        elif func_name == 'decrypt':
            try:
                plain = base64.b64decode(plain)
                result = func(plain, privkey).decode()
            except:
                result = '密文错误，无法解密'

        elif func_name == 'sign':
            result = base64.b64encode(func(plain.encode(), privkey, 'SHA-1')).decode()

        else:
            try:
                signature = base64.b64decode(signature)
                result = str(func(plain.encode(), signature, pubkey))
            except:
                result = 'false'
        return result

    def show_dialog(self):
        """show error to user"""
        QMessageBox.warning(self, "error", "error", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = RSA()
    sys.exit(app.exec_())
