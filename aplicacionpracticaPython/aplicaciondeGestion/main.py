'''
Created on 31 mar. 2020

@author:Jesus
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas01 import ventana_principal, ventana_listado_juegos, ventana_registrar_juegos,\
    ventana_list_widget, ventana_table_widget, ventana_editar_juegos
import sys
from modelo.clases import Juego
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
from _functools import partial



lista_resultado = None

#inicio definicion funciones

def registrar_juego():
    juego = Juego
    juego.tipodejuego = ui_registrar_juego.entrada_tipo_juego.text()
    juego.nombrejuego = ui_registrar_juego.entrada_nombre_juego.text()
    juego.plataforma = ui_registrar_juego.entrada_tipo_plataforma.text()
    juego.añosalida = ui_registrar_juego.entrada_anio_juego.text()
    juego.precio = ui_registrar_juego.entrada_precio_juego.text()

    
    #checkbox
    if ui_registrar_juego.checkbox_digital.isChecked():
        juego.digital = True
    else:   
        juego.digital = False
    #combo
    indice_seleccionado = ui_registrar_juego.combo_edicion.currentIndex()
    juego.edicion = ui_registrar_juego.combo_edicion.itemText(indice_seleccionado)
    
    #radio button
    if ui_registrar_juego.radio_tarjeta_credito.isChecked():
        juego.pago = "Tarjeta Credito"
        
    if ui_registrar_juego.radio_paypal.isChecked():
        juego.pago = "Paypal"
    
    
    operaciones_bd.registro_juego(juego)
    QMessageBox.about(MainWindow,"Info","Registro juego OK")
    
    
    
def mostrar_registro_juegos():
    ui_registrar_juego.setupUi(MainWindow)
    ui_registrar_juego.boton_resgistrar_juego.clicked.connect(registrar_juego)
    
def mostrar_listado_juegos():
    ui_listar_juego.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_juegos()
    texto = ""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " Tipo de Juego:  " + l[1] + " Nombre Juego: " + l[2] + " Plataforma: " + l[3] + " Año: " + str(l[4]) + " Precio: " + str(l[5]) + " Digital: " + str(l[6]) + " Edicion: " + str(l[7])+ " Opcion Pago: " + str(l[8]) +"\n"  
    ui_listar_juego.listado_juegos.setText(texto)
    
    
def mostrar_list_widget():
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_juegos()
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_juegos.addItem(str(l[0]) + " Tipo de Juego: " + str(l[1]) + " Nombre Juego: " + str(l[2]) + " Plataforma: " + str(l[3]) + " Año: " + str(l[4]) + " Precio: " + str(l[5]) + " Digital: " + str(l[6]) + " Edicion: " + str(l[7]) + " Opcion Pago: " + str(l[8]))
    ui_ventana_list_widget.list_widget_juegos.itemClicked.connect(mostrar_registro)
    
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_juegos.currentRow()
    texto = ""
    texto += " Tipo de Juego" + lista_resultado[indice_seleccionado][1] + "\n"
    texto += " Nombre Juego: " + lista_resultado[indice_seleccionado][2] + "\n"
    texto += " Plataforma: " + lista_resultado[indice_seleccionado][3] + "\n"
    texto += " Año: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += " Precio: " + str(lista_resultado[indice_seleccionado][5]) + "\n"
    texto += " Digital: " + str(lista_resultado[indice_seleccionado][6]) + "\n"
    texto += " Edicion: " + str(lista_resultado[indice_seleccionado][7]) + "\n"
    texto += " Opcion Pago : " + str(lista_resultado[indice_seleccionado][8])
    QMessageBox.about(MainWindow,"Info", texto)
    
def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    juegos = operaciones_bd.obtener_juegos()
    fila = 0
    for l in juegos:
        ui_ventana_table_widget.tabla_juegos.insertRow(fila)
        #para añadir las celdas correspondientes
        columna_indice = 0
        for valor in l:
            
            if columna_indice == 6:
                if valor == 0:
                    valor = "NO"
                else: valor = "SI"
                
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_juegos.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #para meter boton de borrar
        boton_borrar = QPushButton("Borrar")
        boton_borrar.clicked.connect(partial(borrar_juego,l[0]))
        ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,9,boton_borrar)
        
        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_juego,l[0],l[2]))
        ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,10,boton_editar)
        
        fila += 1
        
def editar_juego(id,juego):
    QMessageBox.about(MainWindow,"Info","Vas a editar un registro de ID: " + str(id) + " Juego: " + juego)
    ui_ventana_editar_juegos.setupUi(MainWindow)
    #sacar de base de datos toda la informacion a editar
    juego_a_editar = operaciones_bd.obtener_juegos_por_id(id)
    ui_ventana_editar_juegos.entrada_tipo_juego.setText(juego_a_editar.tipodejuego)
    ui_ventana_editar_juegos.entrada_nombre_juego.setText(juego_a_editar.nombrejuego)
    ui_ventana_editar_juegos.entrada_tipo_plataforma.setText(juego_a_editar.plataforma)
    ui_ventana_editar_juegos.entrada_anio_juego.setText(str(juego_a_editar.añosalida))
    ui_ventana_editar_juegos.entrada_precio_juego.setText(str(juego_a_editar.precio))
    ui_ventana_editar_juegos.checkbox_digital.setChecked(juego_a_editar.digital)
    ui_ventana_editar_juegos.combo_edicion.setCurrentText(juego_a_editar.edicion)
    
    if juego_a_editar.digital :
        ui_ventana_editar_juegos.checkbox_digital.setChecked(True)
        
    ui_ventana_editar_juegos.combo_edicion.setCurrentText(juego_a_editar.edicion)
    
    if juego_a_editar.pago == "Tarjeta Credito":
        ui_ventana_editar_juegos.radio_tarjeta_credito.setChecked(True)
    
    if juego_a_editar.pago == "Paypal":
        ui_ventana_editar_juegos.radio_paypal.setChecked(True)
    
    
    
    ui_ventana_editar_juegos.boton_guardar_cambios_juego.clicked.connect(partial(guardar_cambios_juego,juego_a_editar.id))
    

def guardar_cambios_juego(id):
    QMessageBox.about(MainWindow,"Info","Guardar cambios sobre el registro de ID " + str(id))
    juego_guardar_cambios = Juego()
    juego_guardar_cambios.tipodejuego = ui_ventana_editar_juegos.entrada_tipo_juego.text()
    juego_guardar_cambios.nombrejuego = ui_ventana_editar_juegos.entrada_nombre_juego.text()
    juego_guardar_cambios.plataforma = ui_ventana_editar_juegos.entrada_tipo_plataforma.text()
    juego_guardar_cambios.añosalida = ui_ventana_editar_juegos.entrada_anio_juego.text()
    juego_guardar_cambios.precio = ui_ventana_editar_juegos.entrada_precio_juego.text()
    
    if ui_ventana_editar_juegos.checkbox_digital.isChecked():
        juego_guardar_cambios.digital = True
        
    juego_guardar_cambios.edicion = ui_ventana_editar_juegos.combo_edicion.currentText()
    
    #combo
    indice_seleccionado = ui_ventana_editar_juegos.combo_edicion.currentIndex()
    juego_guardar_cambios.edicion = ui_ventana_editar_juegos.combo_edicion.itemText(indice_seleccionado)
    
    #radio button
    if ui_ventana_editar_juegos.radio_tarjeta_credito.isChecked():
        juego_guardar_cambios.pago = "Tarjeta Credito"
        
    if ui_ventana_editar_juegos.radio_paypal.isChecked():
        juego_guardar_cambios.pago = "Paypal"
    
    juego_guardar_cambios.id = id
    
    operaciones_bd.guardar_cambios_juegos(juego_guardar_cambios)
    
    mostrar_table_widget()#mostrar todos los juegos
    

def borrar_juego(id):
    res = QMessageBox.question(MainWindow,"Info","Vas a borrar un registro de ID: " +str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_juego(id)
        mostrar_table_widget()
    
        
def mostrar_inicio():
    ui.setupUi(MainWindow)
    
    
#fin definicion funciones

#inicio aplicacion principal

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()

ui_registrar_juego = ventana_registrar_juegos.Ui_MainWindow()
ui_listar_juego = ventana_listado_juegos.Ui_MainWindow()
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()
ui_ventana_editar_juegos = ventana_editar_juegos.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_insertar_juego.triggered.connect(mostrar_registro_juegos)
ui.submenu_listar_juegos.triggered.connect(mostrar_listado_juegos)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget_juegos.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_juegos.triggered.connect(mostrar_table_widget)



                      
MainWindow.show()
sys.exit(app.exec_())