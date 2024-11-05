import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

server="503-13"
bd='hiperalmacen'
# Conectar a la base de datos
conexion=pyodbc.connect(driver='{SQL Server}', host=server,database=bd)

# Definir tu consulta
query = '''
SELECT 
    P.NivelPedido, 
    SUM(DF.Cantidad) AS cantidad_total
FROM 
    Facturas
INNER JOIN 
    DetalleFactura DF ON Facturas.IdFactura = DF.IdFactura
INNER JOIN 
    Productos P ON DF.Idproducto = P.IdProducto
GROUP BY 
    P.NivelPedido;
'''

# Ejecutar la consulta y cargar los resultados en un DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar la conexión
conexion.close()

# Mostrar el DataFrame
print(df)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(df['NivelPedido'], df['cantidad_total'], color='cornflowerblue')
plt.xlabel('Nivel de Pedido', fontsize=14)
plt.ylabel('Cantidad Total de Productos', fontsize=14)
plt.title('Cantidad Total de Productos por Nivel de Pedido', fontsize=16)
plt.xticks(rotation=45)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()