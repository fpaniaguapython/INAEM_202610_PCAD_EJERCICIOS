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

# CRUD
def create_movie(conexion: sqlite3.Connection, titulo, director, genero):
    cursor = conexion.cursor()
    
    # OPCIÓN 1. Riesgo de SQL Inyection
    # sql = f'INSERT INTO peliculas (titulo, director, genero) VALUES ("{titulo}", "{director}","{genero}")'
    # cursor.execute(sql)

    # OPCIÓN 2. Segura frente a SQL Inyection
    sql = 'INSERT INTO peliculas (titulo, director, genero) VALUES (?, ?, ?)'
    cursor.execute(sql, (titulo, director, genero))

    conexion.commit()

# READ ALL
def read_movies(conexion: sqlite3.Connection):
    cursor = conexion.cursor()
    sql = 'SELECT * FROM peliculas'
    cursor.execute(sql)
    movies = cursor.fetchall()
    return movies

# READ ONE
def read_movie(conexion: sqlite3.Connection, id):
    cursor = conexion.cursor()
    sql = 'SELECT * FROM peliculas WHERE ID = ?'
    cursor.execute(sql, (id,))
    movie = cursor.fetchone()
    return movie

# UPDATE
def update_movie(conexion: sqlite3.Connection, id, titulo, director, genero):
    cursor = conexion.cursor()
    sql = 'UPDATE peliculas SET titulo = ?, director = ?, genero = ? WHERE id = ?'
    cursor.execute(sql, (titulo, director, genero, id))
    conexion.commit()

# DELETE
def delete_movie(conexion: sqlite3.Connection, id):
    cursor = conexion.cursor()
    sql = 'DELETE FROM peliculas WHERE id = ?'
    cursor.execute(sql, (id,))
    conexion.commit()

def cerrar_conexion(conexion: sqlite3.Connection):
    conexion.close()

def _mostrar_menu():
    print('1. Crear película')
    print('2. Listar películas')
    print('3. Buscar película por ID')
    print('4. Actualizar película por ID')
    print('5. Eliminar película por ID')
    print('6. Salir')

if __name__=='__main__':
    # Abrir conexión
    conn = establecer_conexion()

    # Llamar a la creación de la base de datos
    crear_database(conn)

    while True:
        _mostrar_menu()
        opcion = input('Ingrese una opción:')

        match opcion:
            case '1':
                # Solicitar al usuario los datos
                    titulo = input('Título:')
                    director = input('Director:')
                    genero = input('Género:')
                
                    # CREATE pelicula
                    create_movie(conn, titulo, director, genero)
            case '2':
                # READ all
                    movies = read_movies(conn)
                    for movie in movies:
                        print(movie)
                
            case '3':
                # READ one
                    id = int(input('Ingrese el ID de la película a buscar:'))
                    movie = read_movie(conn, id)
                    if movie:
                        print(movie)
                    else:
                        print('No se encontró la película con el ID proporcionado.')
            case '4':
                # UPDATE
                    id = int(input('Ingrese el ID de la película a actualizar:'))
                    titulo = input('Nuevo título:')
                    director = input('Nuevo director:')
                    genero = input('Nuevo género:')
                    update_movie(conn, id, titulo, director, genero)
            case '5':
                # DELETE
                    id = int(input('Ingrese el ID de la película a eliminar:'))
                    delete_movie(conn, id)
            case '6':
                print('Saliendo del programa...')
                exit()
            case _:
                print('Opción inválida. Por favor, seleccione una opción válida.')

    
    
    

    # Cerrar conexión
    cerrar_conexion(conn)