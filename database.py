import mysql.connector

data = []

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_tienda_sadashi")
        return connection

    def insert_db(self, nombre, correo, clave):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_cliente(NOMBRE, CORREO_ELECTRONICO, CLAVE) VALUES (%s,%s,%s)"
        data = (nombre, correo, clave)
        cursor.execute(query, data)
        
        my_connection.commit()

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT  NOMBRE, CORREO_ELECTRONICO, CLAVE FROM TBL_CLIENTE"
        cursor.execute(query)  
        registro = 0
        for fila in cursor:
            data.append(fila)
            print('RESULTADO - BackEnd: ' + str(registro) +" - "+ str(data[registro]))
            registro = registro + 1
        my_connection.close()
