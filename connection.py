import psycopg2

class Connection:
    
	def Connect(self):
		try:
			connection=psycopg2.connect(
				user='postgres', #nombre de usuario
				host='127.0.0.1',
				password='abc12345', #Contraseña de acceso a mysql
				database='test', #Nombre de la base de datos
                port = '5432'
            )
			return connection
	
		except:
			print("Error en la conexion a la base de datos")

	def CloseConnection(self,connection):
		connection.close()

