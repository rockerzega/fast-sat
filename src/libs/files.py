from os import path
from base64 import b64decode

def own_dir() -> str:
  return path.join(path.dirname(__file__), '..', '..', 'data')

def create_file(b64: str, name_file: str):
  # Contenido que deseas guardar en el archivo
  decode_data = b64decode(b64)

  # Obtener la ruta al directorio data/ desde la raíz del proyecto
  path_file = own_dir()

  # Construir la ruta completa al archivo de salida
  out_file = path.join(path_file, name_file)

  # Guardar el archivo en la carpeta data/
  with open(out_file, "wb") as archivo:
    archivo.write(decode_data)

  print(f"El archivo '{out_file}' se ha guardado en la carpeta 'data/'.")
