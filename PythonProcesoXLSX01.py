import pandas as pd

# Reemplaza 'PLANILLA.XLS' con la ruta completa de tu archivo Excel si no esta en el mismo directorio.
# archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\PROCESO\\CONTROL DOCUMENTOS CONST P0034-02.xlsx'
archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\PROCESO\\CONTROL DOCUMENTOS ING DEF P0034-02.xlsx'

# Carga el archivo Excel en un DataFrame
df = pd.read_excel(archivo_excel, sheet_name='TOTAL')


# Filtra el DataFrame para considerar solo documentos con 'ESTATUS DOCUMENTO' igual a 'APROBADO'
df_aprobados = df[df['ESTATUS DOCUMENTO'] == 'APROBADO']

# Muestra las primeras 10 filas con las columnas "PARCIALIDAD" y "ESTATUS DOCUMENTO" de los documentos aprobados
filas_aprobadas = df_aprobados[['PARCIALIDAD', 'ESTATUS DOCUMENTO','C\u00D3DIGO']]

print(filas_aprobadas)