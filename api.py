import requests
from io import BytesIO
from PIL import Image, ImageTk

# Tu llave de acceso para la API de OMDb
API_KEY = "1dee5915"

def obtener_imagen_optimizada(url_poster, titulo_pelicula, tamano=(120, 180)):
    """
    Descarga la imagen desde la URL de OMDb y la procesa en la memoria RAM.
    Mantiene los parámetros originales para no romper los imports de tus vistas.
    """
    if url_poster and url_poster != "N/A":
        try:
            # Petición HTTP directa para obtener los bytes de la imagen
            img_res = requests.get(url_poster, timeout=5)
            
            # Carga la imagen directamente desde el flujo de bytes en memoria
            img_d = Image.open(BytesIO(img_res.content))
            
            # Redimensiona la imagen al tamaño de tu tarjeta de la interfaz
            img_d = img_d.resize(tamano, Image.Resampling.LANCZOS)
            
            # La convierte al formato compatible con Tkinter
            return ImageTk.PhotoImage(img_d)
        except:
            # Si falla la red o la imagen está corrupta, retorna None para poner el botón de texto
            return None
    return None