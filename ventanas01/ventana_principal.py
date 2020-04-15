# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 180, 371, 121))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"MV Boli\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuJuegos = QtWidgets.QMenu(self.menubar)
        self.menuJuegos.setObjectName("menuJuegos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_insertar_musica = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_musica.setObjectName("submenu_insertar_musica")
        self.submenu_listar_juegos = QtWidgets.QAction(MainWindow)
        self.submenu_listar_juegos.setObjectName("submenu_listar_juegos")
        self.submenu_insertar_juego = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_juego.setObjectName("submenu_insertar_juego")
        self.submenu_insertar_canciones = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_canciones.setObjectName("submenu_insertar_canciones")
        self.submenu_insertar_anio = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_anio.setObjectName("submenu_insertar_anio")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_list_widget_juegos = QtWidgets.QAction(MainWindow)
        self.submenu_list_widget_juegos.setObjectName("submenu_list_widget_juegos")
        self.submenu_table_widget_juegos = QtWidgets.QAction(MainWindow)
        self.submenu_table_widget_juegos.setObjectName("submenu_table_widget_juegos")
        self.menuJuegos.addAction(self.submenu_insertar_juego)
        self.menuJuegos.addAction(self.submenu_listar_juegos)
        self.menuJuegos.addAction(self.submenu_list_widget_juegos)
        self.menuJuegos.addAction(self.submenu_table_widget_juegos)
        self.menuJuegos.addAction(self.submenu_inicio)
        self.menubar.addAction(self.menuJuegos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Aplicacion gestión de juegos"))
        self.menuJuegos.setTitle(_translate("MainWindow", "Juegos"))
        self.submenu_insertar_musica.setText(_translate("MainWindow", "Insertar Musica"))
        self.submenu_listar_juegos.setText(_translate("MainWindow", "Listar Juegos"))
        self.submenu_insertar_juego.setText(_translate("MainWindow", "Insertar Juego"))
        self.submenu_insertar_canciones.setText(_translate("MainWindow", "Insertar Canciones"))
        self.submenu_insertar_anio.setText(_translate("MainWindow", "Insertar año"))
        self.submenu_inicio.setText(_translate("MainWindow", "Inicio"))
        self.submenu_list_widget_juegos.setText(_translate("MainWindow", "Listar Juegos List Widget"))
        self.submenu_table_widget_juegos.setText(_translate("MainWindow", "Listar Juegos Table Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
