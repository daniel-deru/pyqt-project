from PyQt5.QtGui import qAlpha
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QCalendarWidget, QLabel
import sys
from PyQt5 import uic

class Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("calendar.ui", self)

        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")

        self.calendar.selectionChanged.connect(self.calendar_date)

    def calendar_date(self):
        date_selected = self.calendar.selectedDate()
        date_string = str(date_selected.toPyDate())

        self.label.setText(f"date is: {date_string}")


def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()