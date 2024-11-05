import pandas as pd 
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
# server="503-13"
# bd='hiperalmacen'
# conexion=pyodbc.connect(driver='{SQL Server}', host=server,database=bd)
# consulta=pd.read_sql("SELECT IdCategoria, count(IdProducto) as 'cantidad' from Productos group by IdCategoria",conexion)
# df=pd.DataFrame(consulta)
# idcategoria = df['IdCategoria']

# nc=df['nombrecat']
# plt.plot(idcategoria,nc)
# plt.show()

# server = "503-13"
# bd = 'hiperalmacen'
# conexion = pyodbc.connect(driver='{SQL Server}', host=server, database=bd)

# consulta = pd.read_sql("SELECT Productos.IdCategoria, Categorias.NombreCat, COUNT(Productos.IdProducto) AS cantidad FROM  Productos LEFT OUTER JOIN  Categorias WITH (NOLOCK) ON Productos.IdCategoria = Categorias.IdCategoria GROUP BY  Productos.IdCategoria,  Categorias.NombreCat", conexion)
# df = pd.DataFrame(consulta)

#conexion.clone()
# idcategoria = df['IdCategoria']  
# nomcate = df['NombreCat'] 
# nc = df['cantidad']  

# plt.bar(nomcate, nc)
# #plt.plot(nomcate, nc)
# plt.xlabel('ID Categoria')
# plt.ylabel('Cantidad')
# plt.title('Cantidad de Productos por Categoría')
# plt.show()


#Grafico de lineas o line Plot - se puede iniciar a generar la grafica

# nombres = np.array(['Tania','Jose','Camila','Simon'])
# cantidad = np.array([34,12,34,45])
# plt.plot(nombres, cantidad) 
# plt.bar(nombres,cantidad,color='blue')
# plt.show()

#Grafico de lineas o line Plot - se puede iniciar a generar la grafica

# nombres = np.array(['Tania','Jose','Camila','Simon'])
# cantidad = np.array([34,12,34,45])
# nom = np.array(['Tania','Jose','Camila','Simon'])
# cant = np.array([34,12,34,45])

# plt.subplot(1,2,1)
# plt.plot(nombres, cantidad)

# plt.subplot(1,2,2)
# plt.plot(nom, cant)

# plt.show()
