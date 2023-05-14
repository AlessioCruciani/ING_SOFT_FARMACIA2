# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiSconti.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget

import PaginaErroreSconto
from PaginaErroreSconto import Ui_ErroreSconto


class Ui_PaginaAggiungiSconti(object):
    def setupUi(self, PaginaAggiungiSconti):
        PaginaAggiungiSconti.setObjectName("PaginaAggiungiSconti")
        PaginaAggiungiSconti.resize(840, 571)
        PaginaAggiungiSconti.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiProdotto/SfondoAggiungiSconto.png);")
        self.ButtonConfermaSconto = QtWidgets.QPushButton(PaginaAggiungiSconti)
        self.ButtonConfermaSconto.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaSconto.setStyleSheet("background-position: center;\n"
                                                "background-image: url(ImmaginiProgetto/ImmaginiProdotto/ButtonConfermaModifica.png);\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: #20730b;")
        self.ButtonConfermaSconto.setText("")
        self.ButtonConfermaSconto.setObjectName("ButtonConfermaSconto")
        self.ButtonAnnullaSconto = QtWidgets.QPushButton(PaginaAggiungiSconti)
        self.ButtonAnnullaSconto.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaSconto.setStyleSheet("background-position: center;\n"
                                               "background-image: url(ImmaginiProgetto/ImmaginiProdotto/ButtonAnnullaModifica.png);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "border-color: #20730b;")
        self.ButtonAnnullaSconto.setText("")
        self.ButtonAnnullaSconto.setObjectName("ButtonAnnullaSconto")
        self.lECodiceProdotto = QtWidgets.QLineEdit(PaginaAggiungiSconti)
        self.lECodiceProdotto.setGeometry(QtCore.QRect(140, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodiceProdotto.setFont(font)
        self.lECodiceProdotto.setStyleSheet("background: none;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: #20730b;\n"
                                            "text-align: center;")
        self.lECodiceProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodiceProdotto.setObjectName("lECodiceProdotto")
        self.labelDNMcodiceProdotto = QtWidgets.QLabel(PaginaAggiungiSconti)
        self.labelDNMcodiceProdotto.setGeometry(QtCore.QRect(140, 160, 261, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNMcodiceProdotto.setFont(font)
        self.labelDNMcodiceProdotto.setStyleSheet("background: transparent;\n"
                                                  "color: #20730b;")
        self.labelDNMcodiceProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDNMcodiceProdotto.setObjectName("labelDNMcodiceProdotto")
        self.lEPercentualeSconto = QtWidgets.QLineEdit(PaginaAggiungiSconti)
        self.lEPercentualeSconto.setGeometry(QtCore.QRect(460, 180, 261, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lEPercentualeSconto.setFont(font)
        self.lEPercentualeSconto.setStyleSheet("background: none;\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 5px;\n"
                                               "border-color: #20730b;\n"
                                               "text-align: center;")
        self.lEPercentualeSconto.setAlignment(QtCore.Qt.AlignCenter)
        self.lEPercentualeSconto.setObjectName("lEPercentualeSconto")
        self.labelDNM_2 = QtWidgets.QLabel(PaginaAggiungiSconti)
        self.labelDNM_2.setGeometry(QtCore.QRect(460, 160, 261, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNM_2.setFont(font)
        self.labelDNM_2.setStyleSheet("background: transparent;\n"
                                      "color: #20730b;")
        self.labelDNM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDNM_2.setObjectName("labelDNM_2")

        self.retranslateUi(PaginaAggiungiSconti)
        QtCore.QMetaObject.connectSlotsByName(PaginaAggiungiSconti)



    def retranslateUi(self, PaginaAggiungiSconti):
        _translate = QtCore.QCoreApplication.translate
        PaginaAggiungiSconti.setWindowTitle(_translate("PaginaAggiungiSconti", "Form"))
        self.labelDNMcodiceProdotto.setText(_translate("PaginaAggiungiSconti", "CODICE PRODOTTO"))
        self.labelDNM_2.setText(_translate("PaginaAggiungiSconti", "PERCENTUALE SCONTO"))

    def controllaCodiceProdotto(self):


        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceProdotto = self.lECodiceProdotto.text()

        queryRicercaProdotto = "SELECT prodotto.IDProdotto FROM prodotto WHERE prodotto.IDProdotto = '" + str(codiceProdotto) + "'"
        mycursor.execute(queryRicercaProdotto)
        risultatoRicercaProdotto = mycursor.fetchall()

        codiceProdottoEsistente = None

        for row in risultatoRicercaProdotto:
            codiceProdottoEsistente = row[0]

        if codiceProdottoEsistente != None:
            return 1
        else:
            return 0




    def creaSconto(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        percentualeSconto = self.lEPercentualeSconto.text()

        queryRicercaPercentuale = "SELECT sconto.IDSconto FROM sconto WHERE sconto.PercentualeSconto = '" + str(percentualeSconto) + "'"
        mycursor.execute(queryRicercaPercentuale)
        risultatoRicercaPercentuale = mycursor.fetchall()

        codiceScontoEsistente = None

        for row in risultatoRicercaPercentuale:
            codiceScontoEsistente = row[0]

        if codiceScontoEsistente != None:
            self.aggiornaScontoProdotto(codiceScontoEsistente)
        else:
            queryCreaNuovoSconto = "INSERT INTO sconto VALUES ('', " + str(percentualeSconto) + ")"
            mycursor.execute(queryCreaNuovoSconto)
            mydb.commit()

            queryIDScontoMax = "SELECT MAX(sconto.IDSconto) FROM sconto"
            mycursor.execute(queryIDScontoMax)
            risultatoIDScontoMax = mycursor.fetchall()

            ultimoCodiceSconto = 0

            for riga in risultatoIDScontoMax:
                ultimoCodiceSconto = riga[0]

            self.aggiornaScontoProdotto(ultimoCodiceSconto)

    def aggiornaScontoProdotto(self, codiceSconto):
        codiceProdotto = self.lECodiceProdotto.text()

        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        queryAggiornaScontoProdotto = "UPDATE prodotto SET prodotto.IDSconto = '" + str(codiceSconto) + "' WHERE prodotto.IDProdotto = '" + str(codiceProdotto) + "'"
        mycursor.execute(queryAggiornaScontoProdotto)
        mydb.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaAggiungiSconti = QtWidgets.QWidget()
    ui = Ui_PaginaAggiungiSconti()
    ui.setupUi(PaginaAggiungiSconti)
    PaginaAggiungiSconti.show()



    sys.exit(app.exec_())