from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5 import uic
import sys
from utils import LoadDataFrom, SaveDocx, SaveTXT
from summarize import summarize
from docx import Document
import requests

form_class = uic.loadUiType("form.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.method = 0
        self.cbBMethod.addItems(['textrank', 'lexrank', 'luhn', 'reduction', 'sumbasic', 'kl', 'edmundson'])
        self.btnBrowse.clicked.connect(self.Browse)
        self.cbBMethod.currentIndexChanged.connect(self.selectionchange)
        self.btnSummary.clicked.connect(self.Summary)
        self.btnSave.clicked.connect(self.Save)
        self.textSource = ''
        self.textSumm = ''
        
    def Browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.txt, *.doc, *.docx, *.html)", options=options)
        if(fileName):
            self.txtFilepath.setText(fileName)
            textOrigin = LoadDataFrom(fileName)
            self.txtOriginal.setPlainText(textOrigin)
            self.textSource = textOrigin
    
    def selectionchange(self, i):
        self.method = i
        print('current method %d: %s' % (i , self.cbBMethod.currentText()))

    def Summary(self):
        textSumm = summarize(self.textSource, sentences_count=3, sum_index= self.method)
        # dic = {'text': self.textSource}
        # respond = requests.post('http://localhost:5555/summary', json=dic)
        # textSumm = respond.json()['key']
        self.txtSummary.setPlainText(textSumm)
        self.textSumm = textSumm

    def Save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File", "",
                "All Files (*);;Text Files (*.txt);;MS Word Files (*.docx)", options=options)
        if fileName:
            if(fileName.split('.')[-1] == 'doc' or 
                fileName.split('.')[-1] == 'docx'):
                SaveDocx(fileName, self.textSumm)
            else:
                SaveTXT(fileName, self.textSumm)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    
    app.exec_()