import sqlite3

def establecer_conexion():
    conexion = sqlite3.connect('peliculas.db')
    return conexion

def crear_database(conexion: sqlite3.Connection):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            director TEXT NOT NULL,
            genero TEXT NOT NULL
        )''')
    conexion.commit()

def create_movie(conexion: sqlite3.Connection, titulo, director, genero):
    cursor = conexion.cursor()
    
    # OPCIÓN 1. Riesgo de SQL Inyection
    # sql = f'INSERT INTO peliculas (titulo, director, genero) VALUES ("{titulo}", "{director}","{genero}")'
    # cursor.execute(sql)

    # OPCIÓN 2. Segura frente a SQL Inyection
    sql = 'INSERT INTO peliculas (titulo, director, genero) VALUES (?, ?, ?)'
    cursor.execute(sql, (titulo, director, genero))

    conexion.commit()

def cerrar_conexion(conexion: sqlite3.Connection):
    conexion.close()

if __name__=='__main__':
    # Abrir conexión
    conn = establecer_conexion()

    # Llamar a la creación de la base de datos
    crear_database(conn)

    # Solicitar al usuario los datos
    titulo = input('Título:')
    director = input('Director:')
    genero = input('Género:')

    # CREATE pelicula
    create_movie(conn, titulo, director, genero)

    # Cerrar conexión
    cerrar_conexion(conn)