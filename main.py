import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QLineEdit, QPushButton, \
    QTableWidgetItem, QComboBox, QMessageBox, QTableWidget, QGridLayout


class MyWidget(QMainWindow):  # Главнео окно, с отображением всей библиотеки и кнопки с 3 разделами
    def __init__(self):
        super().__init__()
        uic.loadUi("UI1.ui", self)

        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()

        self.setWindowTitle('Кофе')

        query = 'SELECT * FROM information'
        res = self.cur.execute(query).fetchall()
        self.statusBar().showMessage('')
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'Сорт', 'Степень прожарки', 'Молотый/В зернах', 'Вкус', 'Цена', 'Объем'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
