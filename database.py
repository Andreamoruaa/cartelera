import sqlite3
import os

CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(CARPETA_PROYECTO, "biblioteca.db")

def iniciar_base_datos():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio TEXT,
            tipo TEXT,
            poster_url TEXT,
            calificacion TEXT DEFAULT 'Sin calificar',
            progreso TEXT DEFAULT 'Sin iniciar',
            genero TEXT DEFAULT 'N/A',
            actores TEXT DEFAULT 'N/A'
        )
    """)
    try: cursor.execute("ALTER TABLE peliculas ADD COLUMN genero TEXT DEFAULT 'N/A'")
    except sqlite3.OperationalError: pass 
    try: cursor.execute("ALTER TABLE peliculas ADD COLUMN actores TEXT DEFAULT 'N/A'")
    except sqlite3.OperationalError: pass 
    conexion.commit()
    conexion.close()