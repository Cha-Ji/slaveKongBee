import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 1000, 1200)
        self.setWindowTitle("차지원의 코인노예")
        self.setWindowIcon(QIcon("./model/images/icon.png"))


app = QApplication(sys.argv)    # QApplication 객체
window = MyWindow()
window.show()

app.exec_()  # 이벤트 루프 생성
