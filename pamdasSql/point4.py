import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de Seaborn para estilos más bonitos
sns.set(style="whitegrid")

server = "503-13"
bd = 'hiperalmacen'

# Conectar a la base de datos
conexion = pyodbc.connect(driver='{SQL Server}', host=server, database=bd)

# Definir tu consulta
query = '''
SELECT 
    Comuna, 
    COUNT(*) AS cantidad_clientes
FROM 
    Clientes
GROUP BY 
    Comuna;
'''

# Ejecutar la consulta y cargar los resultados en un DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión
conexion.close()

# Mostrar el DataFrame
print(df)

# Configurar la figura
plt.figure(figsize=(12, 8))

# Crear un gráfico de barras
sns.barplot(data=df, x='Comuna', y='cantidad_clientes', palette='pastel')

# Establecer etiquetas y título
plt.xlabel('Comuna', fontsize=14)
plt.ylabel('Cantidad de Clientes', fontsize=14)
plt.title('Cantidad de Clientes por Comuna', fontsize=16)
plt.xticks(rotation=45)  # Para que las etiquetas en el eje x estén en ángulo
plt.grid(axis='y')

# Mostrar la gráfica
plt.tight_layout()
plt.show()
