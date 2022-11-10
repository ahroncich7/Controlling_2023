import mysql.connector
from mysql.connector import Error


class Dao():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host= "localhost",
                port= 3306,
                user="root",
                password="12Python34*",
                db="bdejemplo"
            )

        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
        finally:
            self.conexion.close()

    def registar_usuario(self, values):
        self.conexion.connect() 
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO usuarios(mail, contraseña, alias, pais) VALUES ('{0}', '{1}', '{2}', '{3}')"
                cursor.execute(sql.format(values[0], values[1], values[2], values[3]))
                self.conexion.commit()
                print("¡Datos registrado!\n")
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.conexion.close()

    def obtener_usuario(self,mail):
        self.conexion.connect()
        if self.conexion.is_connected():  
            try:
                cursor=self.conexion.cursor()
                sql = "SELECT * FROM usuarios WHERE mail=('{0}')"
                cursor.execute(sql.format(mail))
                resultados=cursor.fetchone()
                print("Consulta exitosa...",resultados)
                return resultados
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.conexion.close()

    def eliminar_usuario(self, mail):
        self.conexion.connect()
        if self.conexion.is_connected():  
            try:
                cursor=self.conexion.cursor()
                sql = "DELETE FROM usuarios WHERE mail=('{0}')"
                cursor.execute(sql.format(mail))
                self.conexion.commit()
                print("Eliminacion exitosa...")
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.conexion.close()
                
    def actualizar_usuario(self, mail, values):
        self.conexion.connect()
        if self.conexion.is_connected():  
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE usuarios SET mail = '{0}', contraseña = '{1}', alias = '{2}', pais = '{3}' WHERE mail = '{4}'"
                cursor.execute(sql.format(values[0], values[1], values[2], values[3],mail))
                self.conexion.commit()
                print("¡Registro actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))








dao = Dao()

valores = ["tom@gamil.com", "fff", "messi", "brasil"]
dao.actualizar_usuario("tomilencina@fghd.com",valores)