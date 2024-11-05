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
    C.NombreCli, 
    COUNT(*) AS cantidad_facturas
FROM 
    Clientes C
INNER JOIN 
    Facturas F ON C.Identificacion = F.IdFactura
GROUP BY 
    C.NombreCli
ORDER BY 
    cantidad_facturas DESC;
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
sns.barplot(data=df, x='NombreCli', y='cantidad_facturas', palette='coolwarm')

# Establecer etiquetas y título
plt.xlabel('Nombre del Cliente', fontsize=14)
plt.ylabel('Cantidad de Facturas', fontsize=14)
plt.title('Cantidad de Facturas Registradas por Cliente', fontsize=16)

# Mostrar la cuadrícula
plt.xticks(rotation=45)  # Para evitar superposición de etiquetas
plt.grid(axis='y')

# Ajustar el layout
plt.tight_layout()

# Mostrar la gráfica
plt.show()
