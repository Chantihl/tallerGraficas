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

# Definir tu consulta para contar facturas por porcentaje de descuento
query = '''
SELECT 
    DF.Descuento AS porcentaje_descuento,
    COUNT(DISTINCT F.IdFactura) AS cantidad_facturas
FROM 
    Facturas F
INNER JOIN 
    (SELECT DISTINCT IdFactura, Descuento FROM DetalleFactura) DF ON F.IdFactura = DF.IdFactura
GROUP BY 
    DF.Descuento
ORDER BY 
    DF.Descuento ASC;
'''

# Ejecutar la consulta y cargar los resultados en un DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión
conexion.close()

# Mostrar el DataFrame para verificar que tiene datos
print(df)

# Verificar si el DataFrame está vacío
if df.empty:
    print("No hay datos para mostrar.")
else:
    # Configurar la figura
    plt.figure(figsize=(12, 8))

    # Crear un gráfico de barras
    sns.barplot(data=df, x='porcentaje_descuento', y='cantidad_facturas', palette='coolwarm')

    # Establecer etiquetas y título
    plt.xlabel('Porcentaje de Descuento', fontsize=14)
    plt.ylabel('Cantidad de Facturas', fontsize=14)
    plt.title('Cantidad de Facturas por Porcentaje de Descuento', fontsize=16)

    # Rotar etiquetas del eje x si es necesario
    plt.xticks(rotation=45)

    # Mostrar la cuadrícula
    plt.grid(axis='y')

    # Ajustar el layout
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()
