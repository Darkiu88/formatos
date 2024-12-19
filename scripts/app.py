from PIL import Image
import os

# Definir las rutas de entrada y salida
input_image_path = os.path.join('images', 'imagen.jpg')  # Imagen original
output_image_path = os.path.join('images', 'background.png')  # Imagen convertida

try:
    # Abre la imagen original
    img = Image.open(input_image_path)

    # Guarda la imagen como PNG
    img.save(output_image_path, format="PNG", quality=100, optimize=True)
    print(f"Imagen convertida y guardada en {output_image_path}")
except Exception as e:
    print(f"Error al convertir la imagen: {e}")