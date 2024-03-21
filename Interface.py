import sys

from PyQt6 import QtGui
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt,QThreadPool


from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QSplashScreen,
    QWidget,
)
import time

from main import main




class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        loadUi("Loading.ui",self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        # pixmap=QtGui.QPixmap("app.jfif")
        # self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.03)
            self.progressBar.setValue(i)



class Window(QDialog,QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("DGT TUNIS")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setMinimumSize(600,200)
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        self.Mail,self.Nom,self.Prenom,self.Numero=QLineEdit(self),QLineEdit(self),QLineEdit(self),QLineEdit(self)
        self.Niveau=QComboBox()
        self.Niveau.addItems(["PCEM1","PCEM2","DCEM1","DCEM2","DCEM3","TCEM","Autres"])
        formLayout.addRow("Mail :", self.Mail)
        formLayout.addRow("Nom :", self.Nom)
        formLayout.addRow("Prénom :", self.Prenom)
        formLayout.addRow("Numéro Téléphone :", self.Numero)
        formLayout.addRow("Niveau :", self.Niveau)
        dialogLayout.addLayout(formLayout)

        ok=QPushButton('Ok',self)
        cancel=QPushButton('Cancel',self)
        dialogLayout.addWidget(ok)
        dialogLayout.addWidget(cancel)

        self.msgLabel = QLabel("")
        dialogLayout.addWidget(self.msgLabel)

        self.setLayout(dialogLayout)

        self.thread_manager = QThreadPool()
        self.thread_manager1=QThreadPool()

        ok.clicked.connect(self.click_safely)
        cancel.clicked.connect(self.clicked)



    def click(self):
        if(self.verification()):
                main(self.Mail.text(), self.Nom.text(), self.Prenom.text(), self.Niveau.currentText(), self.Numero.text())
                self.msgLabel.setText("Envoyé avec succés")
                self.Mail.mousePressEvent=self.clicked



    def click_safely(self):
        self.thread_manager.start(self.click)


    def clicked(self,mouseEvent):
        self.Mail.setText("")
        self.Numero.setText("")
        self.Nom.setText("")
        self.Prenom.setText("")
        self.msgLabel.setText("")


    def verification(self):
        verif=True
        if(self.Mail.text()=="") or ("@" not in self.Mail.text() ):
            self.Mail.setStyleSheet("background-color: #aa6d6d")
            verif=False
        else :
            self.Mail.setStyleSheet("background-color: #ffffff")
        if (self.Nom.text() == ""):
            self.Nom.setStyleSheet("background-color: #aa6d6d")
            verif = False
        else :
            self.Nom.setStyleSheet("background-color: #ffffff")
        if (self.Prenom.text() == ""):
            self.Prenom.setStyleSheet("background-color: #aa6d6d")
            verif = False
        else :
            self.Prenom.setStyleSheet("background-color: #ffffff")
        if (self.Numero.text() == ""):
            self.Numero.setStyleSheet("background-color: #aa6d6d")
            verif = False
        else :
            self.Numero.setStyleSheet("background-color: #ffffff")
        if(self.msgLabel.text()!=""):
            self.msgLabel.setText("")
        return verif



if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()
    splash.progress()

    window = Window()
    window.show()
    #
    splash.finish(window)
    app.exec()


