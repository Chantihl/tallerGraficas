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
    P.IVA, 
    SUM(DF.Cantidad) AS cantidad_total
FROM 
    DetalleFactura DF
INNER JOIN 
    Productos P ON DF.IdProducto = P.IdProducto
GROUP BY 
    P.IVA;
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
sns.barplot(data=df, x='IVA', y='cantidad_total', palette='viridis')

# Establecer etiquetas y título
plt.xlabel('IVA (%)', fontsize=14)
plt.ylabel('Cantidad Total de Productos', fontsize=14)
plt.title('Cantidad de Productos por IVA Asignado', fontsize=16)
plt.xticks(rotation=45)  
plt.grid(axis='y')

# Mostrar la gráfica
plt.tight_layout()
plt.show()
