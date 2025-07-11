# -*- coding: utf-8 -*-
"""Te damos la bienvenida a Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Sección nueva

# Sección nueva
"""

import pandas as pd
from google.colab import files

# ✅ Paso 3: Subir archivo CSV desde tu equipo
print("🔼 Selecciona el archivo .csv para subirlo:")
uploaded = files.upload()  # Muestra el diálogo para subir archivos

# ✅ Paso 4: Obtener el nombre del archivo cargado
csv_file = next(iter(uploaded))  # toma el primer archivo subido

# ✅ Paso 5: Leer archivo CSV en un DataFrame
df = pd.read_csv(csv_file)

# ✅ Paso 6: Definir nombre de salida para el archivo Excel
excel_file = csv_file.replace('.csv', '.xlsx')

# ✅ Paso 7: Guardar el DataFrame como archivo Excel
df.to_excel(excel_file, index=False, engine='openpyxl')

# ✅ Paso 8: Descargar el archivo Excel convertido
print("📥 Descargando archivo Excel convertido...")
files.download(excel_file)