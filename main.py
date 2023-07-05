import os
import requests
from PIL import Image


def descargar_imagen(url, nombre_archivo):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)


def convertir_a_webp(nombre_archivo):
    imagen = Image.open(nombre_archivo)
    nombre_archivo_webp = os.path.splitext(nombre_archivo)[0] + '.webp'
    imagen.save(nombre_archivo_webp, 'webp')
    imagen.close()


def descargar_y_convertir_imagenes(imagenes):
    for i, url in enumerate(imagenes):
        nombre_archivo = f'{i}.jpg'
        descargar_imagen(url, nombre_archivo)
        convertir_a_webp(nombre_archivo)
        os.remove(nombre_archivo)
        print(f'Imagen {i+1}/{len(imagenes)} descargada y convertida.')


# Lista de URLs de las imágenes que deseas descargar y convertir
urls_imagenes = [
    'https://example.com/imagen1.jpg',
    'https://example.com/imagen2.jpg',
    'https://example.com/imagen3.jpg'
]

descargar_y_convertir_imagenes(urls_imagenes)
