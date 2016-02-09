import sys
from PySide.QtCore import *
from PySide.QtGui import *
from Tool import View
import csv

"""
Ein Csv-File kann eingelesen werden indem in Textfeld der Dateiname steht.
Dabei wird der Dialekt des Csv-Files erkannt und im Feld unterhalb ausgegeben.
@date: 2016-01-16
@author: Melanie Goebel
"""
class Controller(QWidget):
    def __init__(self):
        """
        Setzt den vorhanden Button auf seine Tätigkeit und erstellt die Anzeige
        """
        super().__init__(None)
        self.current = 0

        self.myForm = View.Ui_Widget()
        self.myForm.setupUi(self)

        self.myForm.pushButton.clicked.connect(self.read)


    def read(self):
        """
        Lesen eines CSV-Files und ausgeben in ein Textfeld
        """
        text = ''
        file = self.myForm.textEdit.toPlainText()
        # Überprüfung ob die Datei mit csv endet. => sonst kein CSV-File
        if file.endswith(".csv") == False:
            self.myForm.label.setText("Nur Dateiendung .csv erlaubt.")
        else:
            try:
                #Öffnen des Files
                with open(file, 'rt') as csvfile:
                    self.myForm.label.setText(" ")
                    #Überprüfen welcher Dialekt verwendet wird
                    dialect = csv.Sniffer().sniff(csvfile.read(1024))
                    csvfile.seek(0)
                    spamreader = csv.reader(csvfile, dialect)
                    #Zeilenweises herauslesen mit einen Zeilenumbruch dazwischen (Spalten mit Beistrichen)
                    for row in spamreader:
                        text += ",".join(row) + "\n"
            except FileNotFoundError:
               # Fehlermeldung wenn die Datei nicht gefunden werden kann
               self.myForm.label.setText("Datei konnte nicht gefunden werden.")

        self.myForm.textBrowser.setText(text)
