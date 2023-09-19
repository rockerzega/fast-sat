from os import path, remove, makedirs
from base64 import b64decode

def own_dir() -> str:
  return path.normpath(path.join(path.dirname(__file__), '..', '..', 'data'))

def create_file(b64: str, name_file: str):
  try:
    # Contenido que deseas guardar en el archivo
    decode_data = b64decode(b64)

    # Obtener la ruta al directorio data/ desde la raíz del proyecto
    path_file = own_dir()
    
    # Crea la carpeta data/ si no existe
    if not path.exists(path_file):
      makedirs(path_file)
      
    # Construir la ruta completa al archivo de salida
    out_file = path.join(path_file, name_file)

    # Guardar el archivo en la carpeta data/
    with open(out_file, "wb") as archivo:
      archivo.write(decode_data)

    print(f"El archivo '{out_file}' se ha guardado en la carpeta 'data/'.")
  except Exception as error:
    raise f'Error al crear el archivo {str(error)}'

def delete_file(name: str):
  path_file = own_dir()
  out_file = path.join(path_file, name)
  if path.exists(out_file):
    remove(out_file)
    print(f"El archivo '{out_file}' se ha eliminado de la carpeta 'data/'.")
  else:
    print(f"El archivo '{out_file}' no existe en la carpeta 'data/'.")
