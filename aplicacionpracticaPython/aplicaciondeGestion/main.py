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
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton, QFileDialog,\
    QPixmap, QLabel
from _functools import partial
import shutil #facilidad para copiar archivos digitales
from pathlib import Path
from validadores import validadores_juego
from cProfile import label



lista_resultado = None

#inicio definicion funciones

def registrar_juego():
    juego = Juego()
    
    juego.tipodejuego = ui_registrar_juego.entrada_tipo_juego.text()
    juego.tipodejuego = juego.tipodejuego.strip()
    #validador tipo
    resultado_validar_tipo = validadores_juego.validar_tipo(juego.tipodejuego)
    if resultado_validar_tipo == None :
        ui_registrar_juego.label_error_tipo.setText("<font color='red'>Tipo Incorrecto</font>")
        return
    else:
        ui_registrar_juego.label_error_tipo.clear()
    
    juego.nombrejuego = ui_registrar_juego.entrada_nombre_juego.text()
    juego.nombrejuego = juego.nombrejuego.strip()#eliminar espacios en blanco al principio
    #validador nombre
    resultado_validar_nombre = validadores_juego.validar_nombre(juego.nombrejuego)
    if resultado_validar_nombre == None :
        ui_registrar_juego.label_error_nombre.setText("<font color='red'>Nombre Incorrecto</font>")
        return
    else:
        ui_registrar_juego.label_error_nombre.clear()
        
    juego.plataforma = ui_registrar_juego.entrada_tipo_plataforma.text()
    juego.plataforma = juego.plataforma.strip()
    #validador plataforma
    resultado_validar_plataforma = validadores_juego.validar_plataforma(juego.plataforma)
    if resultado_validar_plataforma == None :
        ui_registrar_juego.label_error_plataforma.setText("<font color='red'>Plataforma Incorrecta</font>")
        return
    else:
        ui_registrar_juego.label_error_plataforma.clear()
    
    juego.añosalida = ui_registrar_juego.entrada_anio_juego.text()
    juego.añosalida = juego.añosalida.strip()
    #validador año
    resultado_validar_anio = validadores_juego.validar_anio(juego.añosalida)
    if resultado_validar_anio == None :
        ui_registrar_juego.label_error_anio.setText("<font color='red'>Año Incorrecto</font>")
        return
    else:
        ui_registrar_juego.label_error_anio.clear()
    
    juego.precio = ui_registrar_juego.entrada_precio_juego.text()
    juego.precio = juego.precio.strip()
    #validador precio
    resultado_validar_precio = validadores_juego.validar_precio(juego.precio)
    if resultado_validar_precio == None :
        ui_registrar_juego.label_error_precio.setText("<font color='red'>Precio Incorrecto</font>")
        return
    else:
        ui_registrar_juego.label_error_precio.clear()

    
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
    
    id_imagen = operaciones_bd.registro_juego(juego)
    #guardar imagen temporal renombrandola al id del registro, para saber
    #que dicha imagen es la asociada al registro
    
    #solo se mueve la imagen si existe
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/"+  str(id_imagen) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)
    
    QMessageBox.about(MainWindow,"Info","Registro juego OK")
    
def seleccionar_caratula():
    archivo = QFileDialog.getOpenFileName(MainWindow)  
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ancho_label_imagen = ui_registrar_juego.label_imagen.width()
    alto_label_imagen = ui_registrar_juego.label_imagen.height()
    #redimensionar a ancho
    #pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    #ui_registrar_juego.label_imagen.setPixmap(pixmap_redim)
    #redimensionar por alto     
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_registrar_juego.label_imagen.setPixmap(pixmap_redim)
    #redimensionar por alto y ancho
    #pixmap_redim = pixmap.scaled(ancho_label_imagen,alto_label_imagen)
    #ui_registrar_juego.label_imagen.setPixmap(pixmap_redim)
    
def mostrar_registro_juegos():
    ui_registrar_juego.setupUi(MainWindow)
    ui_registrar_juego.boton_resgistrar_juego.clicked.connect(registrar_juego)
    ui_registrar_juego.boton_seleccionar_archivo.clicked.connect(seleccionar_caratula)
    ui_registrar_juego.label_error_tipo.clear()
    ui_registrar_juego.label_error_nombre.clear()
    ui_registrar_juego.label_error_plataforma.clear()
    ui_registrar_juego.label_error_anio.clear()
    ui_registrar_juego.label_error_precio.clear()
    
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
        ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,10,boton_borrar)
        
        boton_editar = QPushButton("Editar")
        boton_editar.clicked.connect(partial(editar_juego,l[0],l[2]))
        ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,11,boton_editar)
        
        #mostrar una miniatura
        label_miniatura = QLabel()
        ruta_imagen = "imagenes/" + str(l[0]) + ".jpg"
        objeto_path = Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe == True:
            pixmap = QPixmap(ruta_imagen)
            pixmap_redim = pixmap.scaledToHeight(40)
            label_miniatura.setPixmap(pixmap_redim)
            ui_ventana_table_widget.tabla_juegos.setCellWidget(fila,9,label_miniatura)
        
        fila += 1
            
def editar_juego(id,juego):
    juegos = Juego()
    QMessageBox.about(MainWindow,"Info","Vas a editar un registro de ID: " + str(id) + " Juego: " + juego)
    ui_ventana_editar_juegos.setupUi(MainWindow)
    #sacar de base de datos toda la informacion a editar
    juego_a_editar = operaciones_bd.obtener_juegos_por_id(id)
    ui_ventana_editar_juegos.entrada_tipo_juego.setText(juego_a_editar.tipodejuego)
    ui_ventana_editar_juegos.label_error_tipo.clear()
    ui_ventana_editar_juegos.entrada_nombre_juego.setText(juego_a_editar.nombrejuego)
    ui_ventana_editar_juegos.label_error_nombre.clear()
    ui_ventana_editar_juegos.entrada_tipo_plataforma.setText(juego_a_editar.plataforma)
    ui_ventana_editar_juegos.label_error_plataforma.clear()
    ui_ventana_editar_juegos.entrada_anio_juego.setText(str(juego_a_editar.añosalida))
    ui_ventana_editar_juegos.label_error_anio.clear()
    ui_ventana_editar_juegos.entrada_precio_juego.setText(str(juego_a_editar.precio))
    ui_ventana_editar_juegos.label_error_precio.clear()
    juegos.precio = ui_ventana_editar_juegos.entrada_precio_juego.text()
    ui_ventana_editar_juegos.checkbox_digital.setChecked(juego_a_editar.digital)
    ui_ventana_editar_juegos.combo_edicion.setCurrentText(juego_a_editar.edicion)
    
    if juego_a_editar.digital :
        ui_ventana_editar_juegos.checkbox_digital.setChecked(True)
        
    ui_ventana_editar_juegos.combo_edicion.setCurrentText(juego_a_editar.edicion)
    
    if juego_a_editar.pago == "Tarjeta Credito":
        ui_ventana_editar_juegos.radio_tarjeta_credito.setChecked(True)
    
    if juego_a_editar.pago == "Paypal":
        ui_ventana_editar_juegos.radio_paypal.setChecked(True)
        
    #para editar juego y cargar imagen en label imagen
    pixmap = QPixmap("imagenes/"+ str(juego_a_editar.id) +".jpg")
    alto_label_imagen = ui_ventana_editar_juegos.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_juegos.label_imagen.setPixmap(pixmap_redim)
    
    
    
    ui_ventana_editar_juegos.boton_guardar_cambios_juego.clicked.connect(partial(guardar_cambios_juego,juego_a_editar.id))
    ui_ventana_editar_juegos.boton_seleccionar_archivo.clicked.connect(seleccionar_caratula_editar)

def seleccionar_caratula_editar():
    archivo = QFileDialog.getOpenFileName(MainWindow)  
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ancho_label_imagen = ui_ventana_editar_juegos.label_imagen.width()
    alto_label_imagen = ui_ventana_editar_juegos.label_imagen.height()
    #redimensionar a ancho
    #pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    #ui_registrar_juego.label_imagen.setPixmap(pixmap_redim)
    #redimensionar por alto     
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_juegos.label_imagen.setPixmap(pixmap_redim)
    #redimensionar por alto y ancho
    #pixmap_redim = pixmap.scaled(ancho_label_imagen,alto_label_imagen)
    #ui_registrar_juego.label_imagen.setPixmap(pixmap_redim)

def guardar_cambios_juego(id):
    
    juego_guardar_cambios = Juego()
    juego_guardar_cambios.tipodejuego = ui_ventana_editar_juegos.entrada_tipo_juego.text()
    
    resultado_validar_tipo = validadores_juego.validar_tipo(juego_guardar_cambios.tipodejuego)
    if resultado_validar_tipo == None :
        ui_ventana_editar_juegos.label_error_tipo.setText("<font color='red'>Tipo Incorrecto</font>")
        return
    else:
        ui_ventana_editar_juegos.label_error_tipo.clear()
    
    juego_guardar_cambios.nombrejuego = ui_ventana_editar_juegos.entrada_nombre_juego.text()
    
    resultado_validar_nombre = validadores_juego.validar_nombre(juego_guardar_cambios.nombrejuego)
    if resultado_validar_nombre == None :
        ui_ventana_editar_juegos.label_error_nombre.setText("<font color='red'>Nombre Incorrecto</font>")
        return
    else:
        ui_ventana_editar_juegos.label_error_nombre.clear()
    
    juego_guardar_cambios.plataforma = ui_ventana_editar_juegos.entrada_tipo_plataforma.text()
    resultado_validar_plataforma = validadores_juego.validar_plataforma(juego_guardar_cambios.plataforma)
    if resultado_validar_plataforma == None :
        ui_ventana_editar_juegos.label_error_plataforma.setText("<font color='red'>Plataforma Incorrecta</font>")
        return
    else:
        ui_ventana_editar_juegos.label_error_plataforma.clear()
        
    juego_guardar_cambios.añosalida = ui_ventana_editar_juegos.entrada_anio_juego.text()
    resultado_validar_anio = validadores_juego.validar_anio(juego_guardar_cambios.añosalida)
    if resultado_validar_anio == None :
        ui_ventana_editar_juegos.label_error_anio.setText("<font color='red'>Año Incorrecto</font>")
        return
    else:
        ui_ventana_editar_juegos.label_error_anio.clear()
    
    juego_guardar_cambios.precio = ui_ventana_editar_juegos.entrada_precio_juego.text()
    resultado_validar_precio = validadores_juego.validar_precio(juego_guardar_cambios.precio)
    if resultado_validar_precio == None :
        ui_ventana_editar_juegos.label_error_precio.setText("<font color='red'>Precio Incorrecto</font>")
        return
    else:
        ui_ventana_editar_juegos.label_error_precio.clear()
    
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
    
    QMessageBox.about(MainWindow,"Info","Guardar cambios sobre el registro de ID " + str(id))
    operaciones_bd.guardar_cambios_juegos(juego_guardar_cambios)
    
    #solo se mueve la imagen si existe
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/"+  str(id) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)
    
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
ui_editar_juego = ventana_editar_juegos.Ui_MainWindow()
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