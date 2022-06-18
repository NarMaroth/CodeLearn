import mysql.connector

cnx = mysql.connector.connect(
    host ="localhost",
    user="BMateo",
    password="11012001bm",
    database = "Fablab"
)

crs = cnx.cursor()



crs.execute (" CREATE DATABASE IF NOT EXISTS Fablab; ")

crs.execute("USE Fablab")

# Crear tabla Usuarios:
crs.execute ("""
    CREATE TABLE IF NOT EXISTS usuarios(
        nombre_Usuario varchar(20),
        clave varchar(20)
    );
""")

# Crear tabla Cursos:
crs.execute ("""
    CREATE TABLE IF NOT EXISTS cursos(
       nombre_usuario varchar(20),
       curso varchar(20),
       costo int
    );
""")

# Insertar Usuarios
crs.execute ("""
    INSERT INTO usuarios VALUES
        ('Pepe','12345kl'),
        ('Juan','kl12345'),
        ('Ana','clave'),
        ('Maria','evalc'),
        ('Hernesto','contrasena')
""")

# Insertar Cursos
crs.execute ("""
    INSERT INTO cursos VALUES
        ('Pepe','Python',0),
        ('Juan','SQL',50),
        ('Ana','Autocad',100),
        ('Maria','SQL',50),
        ('Hernesto','Python',0)
""")

cnx.commit()


crs.execute("select * from usuarios")
usuarios = crs.fetchall()


crs.execute("""
    SELECT nombre_usuario, costo FROM cursos 
    WHERE curso = "Python" or curso = "SQL";
""")

for i in (crs.fetchall()):
    print(i)




cnx.close()