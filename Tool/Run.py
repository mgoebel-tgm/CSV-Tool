from Tool.Control import *
import csv
"""
Startet die Applikation
@date: 2016-01-16
@author: Melanie Goebel
"""
if __name__ == "__main__":

    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
