import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from load_data import LoadData
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox
from PyQt5 import QtWidgets, uic




class Ui(QtWidgets.QMainWindow, LoadData):
    def __init__(self):
        super(Ui, self).__init__()
        LoadData.__init__(self)
        uic.loadUi('ui.ui', self)

        self.show_crypto()

        self.show_crypto()
        # self.show_mobile_table()
        self.show()


        # init timer
        self.timer = QTimer()
        self.timer.setInterval(10000)  # 10 seconds
        self.timer.timeout.connect(self.show_crypto)
        self.timer.start()


        # # init timer for mobile data
        # self.timer_mobile = QTimer()
        # self.timer_mobile.setInterval(100000)  # 100 seconds
        # self.timer_mobile.timeout.connect(
        #     lambda: self.show_mobile_table() if self.set_mobile_data() else None
        # )
        # self.timer_mobile.start()



    def save_clicked(self):
        # print(self.input_first_name.text())
        self.add_user(
            self.input_first_name.text(),
            self.input_last_name.text()
        )
        self.input_first_name.setText('')
        self.input_last_name.setText('')
        self.show_crypto()

    def show_crypto(self):
        # last_update_label
        self.crypto_table.setRowCount(0)  # Clear the table
        # users = self.get_users()
        crypto = self.get_data()
        if crypto is None:
            QMessageBox.critical(self, "Error", "Cannot get data from API")
            return
        for c in crypto:

            row_position = self.crypto_table.rowCount()
            self.crypto_table.insertRow(row_position)

            self.crypto_table.setItem(
                row_position, 0, QTableWidgetItem(c.name))
            self.crypto_table.setItem(
                row_position, 1, QTableWidgetItem(str(c.open)))
            self.crypto_table.setItem(
                row_position, 2, QTableWidgetItem(str(c.high)))
            self.crypto_table.setItem(
                row_position, 3, QTableWidgetItem(str(c.low)))
            self.crypto_table.setItem(
                row_position, 4, QTableWidgetItem(str(c.close)))
            self.crypto_table.setItem(
                row_position, 5, QTableWidgetItem(str(c.change_percent)))
        # set last_update_label to current time
        self.last_update_label.setText(c.created_at.strftime("%H:%M:%S"))

    # def show_mobile_table(self):
    #     self.mobile_table.setRowCount(0)
    #     data = self.get_mobile_data_db()

    #     for d in data:
    #         row_position = self.mobile_table.rowCount()
    #         self.mobile_table.insertRow(row_position)

    #         self.mobile_table.setItem(
    #             row_position, 1, QTableWidgetItem(d.title))
    #         self.mobile_table.setItem(
    #             row_position, 2, QTableWidgetItem(str(d.black)))
    #         self.mobile_table.setItem(
    #             row_position, 3, QTableWidgetItem(str(d.white)))
    #         self.mobile_table.setItem(
    #             row_position, 4, QTableWidgetItem(str(d.pink)))
    #         self.mobile_table.setItem(
    #             row_position, 5, QTableWidgetItem(str(d.gold)))
    #         self.mobile_table.setItem(
    #             row_position, 6, QTableWidgetItem(str(d.silver)))
            
    #         # 
    #         self.last_mobile_update_lable.setText(d.updated_at.strftime("%H:%M:%S"))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
