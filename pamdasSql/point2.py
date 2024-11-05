import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

server="503-13"
bd='hiperalmacen'
# Conectar a la base de datos
conexion=pyodbc.connect(driver='{SQL Server}', host=server,database=bd)

# Definir tu consulta
query = '''
SELECT 
    P.NombrePro,
    P.Cantidad
FROM 
    Productos P
WHERE 
    P.Cantidad IN (
        SELECT 
            Cantidad
        FROM 
            Productos
        GROUP BY 
            Cantidad
        HAVING 
            COUNT(*) > 1
    )
ORDER BY 
    P.Cantidad;
'''

# Ejecutar la consulta y cargar los resultados en un DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión
conexion.close()

# Mostrar el DataFrame
print(df)

# Configurar la figura
plt.figure(figsize=(12, 8))

# Crear un gráfico de dispersión
sns.scatterplot(data=df, x='Cantidad', y='NombrePro', s=100, color='royalblue', alpha=0.7, edgecolor='black')

# Establecer etiquetas y título
plt.xlabel('Cantidad', fontsize=14)
plt.ylabel('Producto', fontsize=14)
plt.title('Productos con la Misma Cantidad', fontsize=16)
plt.xticks(rotation=45)  # Para que las etiquetas en el eje x estén en ángulo
plt.grid(True)

# Agregar una línea de referencia para cada cantidad
for cantidad in df['Cantidad'].unique():
    plt.axvline(x=cantidad, color='grey', linestyle='--', linewidth=0.8, alpha=0.5)

# Mostrar la gráfica
plt.tight_layout()
plt.show()