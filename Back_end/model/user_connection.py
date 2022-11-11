import mysql.connector
from mysql.connector import Error


class Dao():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host= "localhost",
                port= 3306,
                user="root",
                password="",
                db="controlling"
            )

        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
        finally:
            self.connection.close()

    def insert_user(self, values):
        self.connection.connect() 
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO Usuario (mail, contrasenia, alias, pais) VALUES ('{0}', '{1}', '{2}', '{3}')"
                cursor.execute(sql.format(values[0], values[1], values[2], values[3]))
                self.connection.commit()
                print("¡Datos registrado!\n")
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.connection.close()

    def select_user(self,mail):
        self.connection.connect()
        if self.connection.is_connected():  
            try:
                cursor=self.connection.cursor()
                sql = "SELECT * FROM Usuario WHERE mail=('{0}')"
                cursor.execute(sql.format(mail))
                resultados=cursor.fetchone()
                print("Consulta exitosa...",resultados)
                return resultados
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.connection.close()

    def delete_user(self, mail):
        self.connection.connect()
        if self.connection.is_connected():  
            try:
                cursor=self.connection.cursor()
                sql = "DELETE FROM Usuario WHERE mail=('{0}')"
                cursor.execute(sql.format(mail))
                self.connection.commit()
                print("Eliminacion exitosa...")
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.connection.close()
                
    def update_user(self, mail, values):
        self.connection.connect()
        if self.connection.is_connected():  
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE Usuario SET mail = '{0}', contrasenia = '{1}', alias = '{2}', pais = '{3}' WHERE mail = '{4}'"
                cursor.execute(sql.format(values[0], values[1], values[2], values[3],mail))
                self.connection.commit()
                print("¡Registro actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def count_users_by_country(self):
        self.connection.connect()
        if self.connection.is_connected():  
            try:
                cursor=self.connection.cursor()
                sql = "SELECT pais, COUNT(*) FROM Usuario GROUP BY pais"
                cursor.execute(sql)
                resultados=cursor.fetchall()
                print("Consulta paises exitosa...",resultados)
                return resultados
            except Error as ex:
                print("El error es: ", ex)
            finally:
                self.connection.close()
