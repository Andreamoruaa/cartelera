from tkinter import *
from tkinter import ttk
from database import iniciar_base_datos
from pantallas.home import render_home
from pantallas.library import render_library
from pantallas.details import render_details
from pantallas.stats import render_stats
from pantallas.search import render_search_results

# Inicializar Base de Datos
iniciar_base_datos()

# Listas globales de control de caché
imagenes_cache = []       
cache_busqueda_home = []  

def clear_content():
    global imagenes_cache, cache_busqueda_home
    imagenes_cache.clear() 
    cache_busqueda_home.clear()
    for widget in content_area.winfo_children():
        widget.destroy()

def nav_to(view_name, extra_data=None):
    clear_content()
    if view_name == "Inicio":
        render_home(content_area, nav_to, cache_busqueda_home)
    elif view_name == "Biblioteca":
        render_library(content_area, nav_to, imagenes_cache)
    elif view_name == "Estadisticas":
        render_stats(content_area)
    elif view_name == "Detalles":
        render_details(content_area, extra_data, nav_to)
    elif view_name == "ResultadosBusqueda":
        render_search_results(content_area, extra_data, nav_to, cache_busqueda_home)

# --- INTERFAZ BASE DE TKINTER ---
root = Tk()
root.title("CineTeca")
root.state('zoomed')  
root.configure(bg="#0D0F14")

# Estilos del scroll
style = ttk.Style()
style.theme_use("clam")
style.configure("Vertical.TScrollbar", troughcolor="#0D0F14", background="#252A38", arrowcolor="#6B7280", bordercolor="#0D0F14", thickness=14)

# Menú Lateral
sidebar = Frame(root, bg="#161922", width=240, padx=10)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)  

Label(sidebar, text="CineTeca", font=("Arial", 24, "bold"), bg="#161922", fg="#E8EAF0", pady=35).pack()

for text, view in [("🏠   Inicio", "Inicio"), ("📚   Biblioteca", "Biblioteca"), ("📊   Estadísticas", "Estadisticas")]:
    Button(sidebar, text=text, font=("Arial", 11), bg="#161922", fg="#E8EAF0", relief="flat", anchor="w", padx=25, pady=14, 
           activebackground="#1E2330", activeforeground="#4F8EF7", command=lambda v=view: nav_to(v)).pack(fill="x", pady=2)

# Área de Contenido Principal
content_area = Frame(root, bg="#0D0F14", padx=55, pady=40)
content_area.pack(side="right", fill="both", expand=True)

# Carga inicial
nav_to("Inicio")
root.mainloop()