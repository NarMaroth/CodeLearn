import mysql.connector

# Conection (cnx):
cnx = mysql.connector.connect(
    host ="localhost",
    user="BMateo",
    password="11012001bm",
    database="pythonBBDD"
)


# Cursos: (crs)
crs = cnx.cursor()


# Execute permite instrucciones sql
#   crs.execute(""" """)  // Insertar todo dentro de las triples comillas

crs.execute ("""

    select * from productos;

""")

#- fetchall: Obtiene todo lo que retorne del select
# print(crs.fetchall())   // Imprime una lista de los registros en la tabla
"""
    EJEMPLO:
        productos = crs.fetchall()
        print(productos[0])

        for i in productos:
        print(i)
"""
#- fetchone: Obtiene solo lo del primer SELECT

#- Funcion necesaria para insertar valores en tablas
#   cnx.commit()

# Finalizar la conexion con la base de datos
cnx.close()