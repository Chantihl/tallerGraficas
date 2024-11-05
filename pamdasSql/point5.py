import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Configuración de Seaborn para estilos más bonitos
sns.set(style="whitegrid")

server = "503-13"
bd = 'hiperalmacen'

# Conectar a la base de datos
conexion = pyodbc.connect(driver='{SQL Server}', host=server, database=bd)

# Definir tu consulta
query = '''
SELECT 
    FechaCompra, 
    COUNT(*) AS cantidad_facturas
FROM 
    Facturas
GROUP BY 
    FechaCompra
ORDER BY 
    FechaCompra;
'''

# Ejecutar la consulta y cargar los resultados en un DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión
conexion.close()

# Asegurarse de que la columna 'FechaCompra' sea del tipo datetime
df['FechaCompra'] = pd.to_datetime(df['FechaCompra'])

# Mostrar el DataFrame
print(df)

# Configurar la figura
plt.figure(figsize=(12, 8))

# Crear un gráfico de barras
sns.barplot(data=df, x='FechaCompra', y='cantidad_facturas', color='royalblue')

# Establecer etiquetas y título
plt.xlabel('Fecha de Compra', fontsize=14)
plt.ylabel('Cantidad de Facturas', fontsize=14)
plt.title('Cantidad de Facturas Registradas por Fecha de Compra', fontsize=16)

# Limitar las fechas mostradas
plt.xticks(rotation=45)  # Para que las etiquetas en el eje x estén en ángulo

# Usar formato de fechas en el eje x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Cambia esto a DayLocator, WeekdayLocator, etc. según sea necesario

# Mostrar la cuadrícula
plt.grid(axis='y')

# Ajustar el layout
plt.tight_layout()

# Mostrar la gráfica
plt.show()
