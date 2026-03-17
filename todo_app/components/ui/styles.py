"""
Constantes de estilos para la aplicación.

Este módulo contiene todas las constantes de estilos CSS
utilizadas en los componentes de la aplicación.
"""

# Colores principales de la aplicación
COLORES = {
    "primario": "indigo",
    "exito": "green",
    "advertencia": "yellow",
    "peligro": "red",
    "gris": "gray",
}

# Tamaños de fuente
TAMANIOS = {
    "titulo": "4xl",
    "subtitulo": "2xl",
    "cuerpo": "lg",
    "pequeno": "sm",
}

# Clases CSS reutilizables
CLASES_CONTENEDOR = "max-w-7xl mx-auto px-4"
CLASES_CARTA = "bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow"
CLASES_BOTON_PRIMARIO = "bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition-colors font-medium"
CLASES_BOTON_SECUNDARIO = "bg-gray-100 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-200 transition-colors font-medium"
CLASES_INPUT = "w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-colors"

# Configuración de prioridades
PRIORIDADES = [
    {"value": "baja", "label": "Baja", "color": "green"},
    {"value": "media", "label": "Media", "color": "yellow"},
    {"value": "alta", "label": "Alta", "color": "red"},
]
