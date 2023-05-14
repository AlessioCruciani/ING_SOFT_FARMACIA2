# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginePrenotazioni.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import  mysql.connector


class Ui_PaginaPrenotazioni(object):
    def setupUi(self, PaginaPrenotazioni):
        PaginaPrenotazioni.setObjectName("PaginaScontrini")
        PaginaPrenotazioni.resize(840, 571)
        PaginaPrenotazioni.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/SfondoPrenotazioni.png);")
        self.TablePrenotazioni = QtWidgets.QTableWidget(PaginaPrenotazioni)
        self.TablePrenotazioni.setGeometry(QtCore.QRect(60, 240, 721, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablePrenotazioni.sizePolicy().hasHeightForWidth())
        self.TablePrenotazioni.setSizePolicy(sizePolicy)
        self.TablePrenotazioni.setStyleSheet(
            "background-color: rgb(122, 122, 122);\n"
            "alternate-background-color: rgb(218, 218, 218);\n"
            "background: none;\n"
            "border: 2px solid white;\n"
            "border-bottom-color: #20730b;\n"
            "td: 100px;\n"
            "\n"
            "")
        self.TablePrenotazioni.setObjectName("TableScontrini")
        self.TablePrenotazioni.setColumnCount(6)
        self.TablePrenotazioni.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePrenotazioni.setHorizontalHeaderItem(5, item)
        self.TablePrenotazioni.horizontalHeader().setDefaultSectionSize(119)
        self.ButtonAggiungiPrenotazioni = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonAggiungiPrenotazioni.setGeometry(QtCore.QRect(60, 470, 221, 40))
        self.ButtonAggiungiPrenotazioni.setStyleSheet("background-position: center;\n"
                                                      "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonAggiungiPrenotazioni.png);\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "border-color: #20730b;")
        self.ButtonAggiungiPrenotazioni.setText("")
        self.ButtonAggiungiPrenotazioni.setObjectName("ButtonAggiungiScontrini")

        self.ButtonRimuoviPrenotazioni = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonRimuoviPrenotazioni.setGeometry(QtCore.QRect(60, 520, 220, 40))
        self.ButtonRimuoviPrenotazioni.setStyleSheet("background-position: center;\n"
                                                      "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonRimuoviPrenotazioni.png);\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "border-color: #20730b;")
        self.ButtonRimuoviPrenotazioni.setText("")
        self.ButtonRimuoviPrenotazioni.setObjectName("ButtonRimuoviPrenotazioni")

        self.ButtonAggiungiEsito = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonAggiungiEsito.setGeometry(QtCore.QRect(300, 470, 220, 40))
        self.ButtonAggiungiEsito.setStyleSheet("background-position: center;\n"
                                                      "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonAggiungiEsito.png);\n"
                                                      "border: 2px solid black;\n"
                                                      "border-radius: 10px;\n"
                                                      "border-color: #20730b;")
        self.ButtonAggiungiEsito.setText("")
        self.ButtonAggiungiEsito.setObjectName("ButtonAggiungiEsito")

        self.ButtonModificaPrenotazioni = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonModificaPrenotazioni.setGeometry(QtCore.QRect(300, 520, 220, 40))
        self.ButtonModificaPrenotazioni.setStyleSheet("background-position: center;\n"
                                               "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonModificaPrenotazioni.png);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "border-color: #20730b;")
        self.ButtonModificaPrenotazioni.setText("")
        self.ButtonModificaPrenotazioni.setObjectName("ButtonModificaPrenotazioni")

        self.ButtonCercaPrenotazioni = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonCercaPrenotazioni.setGeometry(QtCore.QRect(500, 160, 220, 40))
        self.ButtonCercaPrenotazioni.setStyleSheet("background-position: center;\n"
                                                   "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonCercaPrenotazioni.png);\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 10px;\n"
                                                   "border-color: #20730b;")
        self.ButtonCercaPrenotazioni.setText("")
        self.ButtonCercaPrenotazioni.setObjectName("ButtonCercaScontrini")
        self.ButtonEsiti = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonEsiti.setGeometry(QtCore.QRect(540, 470, 220, 40))
        self.ButtonEsiti.setStyleSheet("background-position: center;\n"
                                      "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonVisualizzaEsito.png);\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: #20730b;")
        self.ButtonEsiti.setText("")
        self.ButtonEsiti.setObjectName("ButtonEsiti")
        self.ButtonHome = QtWidgets.QPushButton(PaginaPrenotazioni)
        self.ButtonHome.setGeometry(QtCore.QRect(540, 520, 220, 40))
        self.ButtonHome.setStyleSheet("background-position: center;\n"
                                      "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonHome.png);\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: #20730b;")
        self.ButtonHome.setText("")
        self.ButtonHome.setObjectName("ButtonHome")
        self.lineEdit = QtWidgets.QLineEdit(PaginaPrenotazioni)
        self.lineEdit.setGeometry(QtCore.QRect(100, 160, 381, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: none;\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 5px;\n"
                                    "border-color: #20730b;\n"
                                    "text-align: center;")
        self.lineEdit.setObjectName("lineEdit")

        self.caricaDatiPrenotazioni()
        self.ButtonCercaPrenotazioni.clicked.connect(self.cercaDatiPrenotazione)

        self.retranslateUi(PaginaPrenotazioni)
        QtCore.QMetaObject.connectSlotsByName(PaginaPrenotazioni)

    def retranslateUi(self, PaginaPrenotazioni):
        _translate = QtCore.QCoreApplication.translate
        PaginaPrenotazioni.setWindowTitle(_translate("PaginePrenotazioni", "Form"))
        item = self.TablePrenotazioni.horizontalHeaderItem(0)
        item.setText(_translate("PaginePrenotazioni", "Codice Prenotazione"))
        item = self.TablePrenotazioni.horizontalHeaderItem(1)
        item.setText(_translate("PaginePrenotazioni", "Nome Cliente"))
        item = self.TablePrenotazioni.horizontalHeaderItem(2)
        item.setText(_translate("PaginePrenotazioni", "Cognome Cliente"))
        item = self.TablePrenotazioni.horizontalHeaderItem(3)
        item.setText(_translate("PaginePrenotazioni", "Email"))
        item = self.TablePrenotazioni.horizontalHeaderItem(4)
        item.setText(_translate("PaginePrenotazioni", "Data"))
        item = self.TablePrenotazioni.horizontalHeaderItem(5)
        item.setText(_translate("PaginePrenotazioni", "Ora"))


    def caricaDatiPrenotazioni(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        queryTablePrenotazioni = "SELECT * FROM prenotazioni"
        mycursor.execute(queryTablePrenotazioni)
        risultatoQueryPrenotazioni = mycursor.fetchall()
        rigaTabella = 0
        righeTotali = 0

        for row in risultatoQueryPrenotazioni:
            righeTotali += 1

        self.TablePrenotazioni.setRowCount(righeTotali)

        for row in risultatoQueryPrenotazioni:
            self.TablePrenotazioni.verticalHeader().setVisible(bool(0))
            self.TablePrenotazioni.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TablePrenotazioni.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TablePrenotazioni.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TablePrenotazioni.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TablePrenotazioni.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.TablePrenotazioni.setItem(rigaTabella, 5, QtWidgets.QTableWidgetItem(str(row[5])))

            rigaTabella += 1

    def cercaDatiPrenotazione(self):
        richiesta = self.lineEdit.text()
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()
        queryRicercaPrenotazioni = "SELECT * FROM prenotazioni WHERE prenotazioni.NomeCliente = '" + richiesta + "' OR prenotazioni.CognomeCliente = '" + richiesta + "' OR prenotazioni.IDPrenotazioni ='" + richiesta + "'"
        mycursor.execute(queryRicercaPrenotazioni)
        risultatoRicercaPrenotazioni = mycursor.fetchall()

        rigaTabella = 0
        righeTotali = 0

        for row in risultatoRicercaPrenotazioni:
            righeTotali += 1

        self.TablePrenotazioni.setRowCount(righeTotali)

        for row in risultatoRicercaPrenotazioni:
            self.TablePrenotazioni.verticalHeader().setVisible(bool(0))
            self.TablePrenotazioni.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TablePrenotazioni.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TablePrenotazioni.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TablePrenotazioni.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TablePrenotazioni.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.TablePrenotazioni.setItem(rigaTabella, 5, QtWidgets.QTableWidgetItem(str(row[5])))

            rigaTabella += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaPrenotazioni = QtWidgets.QWidget()
    ui = Ui_PaginaPrenotazioni()
    ui.setupUi(PaginaPrenotazioni)
    PaginaPrenotazioni.show()
    sys.exit(app.exec_())