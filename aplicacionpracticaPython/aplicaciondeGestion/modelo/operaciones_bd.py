import mysql.connector
from modelo import constantes_sql, clases

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_videojuegos"
        
        
        )
    return conexion

def registro_juego(juego):
    sql = constantes_sql.SQL_INSERCION_JUEGO
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (juego.tipodejuego , juego.nombrejuego , juego.plataforma , juego.añosalida , juego.precio, juego.digital, juego.edicion, juego.pago)
    cursor.execute(sql , valores_a_insertar)
    conexion.commit()
    id_imagen = cursor.lastrowid
    conexion.disconnect()
    return id_imagen
    
def obtener_juegos():
    sql = constantes_sql.SQL_SELECT_JUEGOS
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect
    return lista_resultado
    
def borrar_juego(id_juego):
    sql = constantes_sql.SQL_BORRAR_JUEGO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_juego,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
def obtener_juegos_por_id(id):
    sql = constantes_sql.SQL_OBTENER_JUEGOS_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    resultado = cursor.fetchone()
    print(resultado)  
    conexion.disconnect()  
    #meter resultado en un objeto de Juego
    juego = clases.Juego()
    juego.id = resultado[0]
    juego.tipodejuego = resultado[1]
    juego.nombrejuego = resultado[2]
    juego.plataforma = resultado[3]
    juego.añosalida = resultado[4]
    juego.precio = resultado[5]
    juego.digital = resultado[6]
    juego.edicion = resultado[7]
    juego.pago = resultado[8]
    
    
    return juego

def guardar_cambios_juegos(juego_guardar_cambios):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_JUEGOS
    conexion = conectar()
    cursor = conexion.cursor()
    val = (juego_guardar_cambios.tipodejuego, juego_guardar_cambios.nombrejuego, juego_guardar_cambios.plataforma, juego_guardar_cambios.añosalida, juego_guardar_cambios.precio, juego_guardar_cambios.digital, juego_guardar_cambios.edicion, juego_guardar_cambios.pago, juego_guardar_cambios.id)
    try:
        cursor.execute(sql,val)
    except Exception as e:
        print(e)
    conexion.commit()
    conexion.disconnect()
    
    
    

    
    
    
    
    