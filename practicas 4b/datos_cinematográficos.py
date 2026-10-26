'''Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.


(Pista 1: Tu array de entrada puede tener la forma…)
(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero)
'''
import numpy as np

# titulo, genero, duración, año, calificación
peliculas = np.array([
['Peli 1', 'Comedia', 120, 1990, 8.5],
['Peli 2', 'Acción', 110, 2005, 7.8],
['Peli 3','Drama', 95, 2010, 6.9],
['Peli 4', 'Comedia', 100, 1985, 7.5],
['Peli 5', 'Acción', 130, 2015, 8.1],
['Peli 6', 'Drama', 115, 2000, 6.7],
['Peli 7', 'Comedia', 90, 1995, 8.2],
['Peli 8','Acción', 105, 2010, 7.4],
['Peli 9', 'Drama', 125, 1980, 6.8],
['Peli 10', 'Comedia', 95, 2000, 8.0]
])

generos, conteo = np.unique(peliculas[:,1], return_counts=True)
print("Los géneros de películas en la lista son: ", generos)
print("-----------")
print("El número de veces que se repiten los géneros en el mismo orden es: ", conteo)
print("-----------")
conteo_des = np.argsort(conteo)[::-1]
print("El orden en los índices de la lista de conteo con más visualizaciones es: ",conteo_des)
genero_popular = generos[conteo_des[0]]
print("-----------")
print("Las veces que se repiten dichos géneros son ", conteo, "con lo que el género popular es :", genero_popular)
print("-----------")

años = (peliculas[:,3])
print("Los años de todas las películas de la lista son :",años)
print("-----------")

decadas = np.unique(peliculas[:,3].astype(int)//10*10)
print("Las décadas de la lista son: ",decadas)
print("-----------")
conteo_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    conteo_decadas.append(conteo)
    print("En la década de ",decada, "se crearon" ,conteo, "películas")
    print("-----------")
todas_pelis = peliculas[:,1]
duraciones = peliculas[:,2]
duracion_media = np.zeros(len(generos))

for i in range(len(generos)):
    duracion_media[i] = np.mean(duraciones[todas_pelis==generos[i]].astype(float))
    print("La duración del género ", generos[i], "es de ", duracion_media[i], "minutos")