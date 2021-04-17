import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb
import pybithumb
import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from volatility import *


class VolatilityWorker(QThread):
    tradingSent = pyqtSignal(str, str, str)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month,
                                now.day) + datetime.timedelta(1)
        ma5 = get_yesterday_ma5(self.ticker)
        target_price = get_target_price(self.ticker)
        wait_flag = False
        print("target price :", target_price)
        while self.alive:
            try:
                now = datetime.datetime.now()
                if mid < now < mid + datetime.timedelta(seconds=10):
                    target_price = get_target_price(self.ticker)
                    mid = datetime.datetime(
                        now.year, now.month, now.day) + datetime.timedelta(1)
                    ma5 = get_yesterday_ma5(self.ticker)

                    wait_flag = False

                if wait_flag == False:
                    current_price = pybithumb.get_current_price(self.ticker)
                    if (current_price > target_price) and (current_price > ma5):
                        wait_flag = True
            except:
                pass
            time.sleep(1)

    def close(self):
        self.alive = False


form_class = uic.loadUiType("View/resource/main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ticker = "BTC"
        self.button.clicked.connect(self.clickBtn)
        self.setWindowTitle("차지원의 매매노예")

    def clickBtn(self):
        if self.button.text() == "매매시작":

            self.button.setText("매매중지")
            self.textEdit.append("------ START ------")

            self.vw = VolatilityWorker(self.ticker)
            self.vw.tradingSent.connect(self.receiveTradingSignal)
            self.vw.start()
        else:
            self.vw.close()
            self.textEdit.append("------- END -------")
            self.button.setText("매매시작")

    def receiveTradingSignal(self, time, type, amount):
        self.textEdit.append(f"[{time}] {type} : {amount}")

    def closeEvent(self, event):
        self.vw.close()
        self.widget.closeEvent(event)
        self.widget_2.closeEvent(event)
        self.widget_3.closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
