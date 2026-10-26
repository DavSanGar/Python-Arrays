'''Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna.
'''


#importamos modulos
import numpy as np

#calificaciones de estudiantes / input
calificaciones = np.array([
[8, 7, 9, 10],
[6, 8, 7, 9],
[9, 9, 8, 8],
[7, 6, 6, 7],
[10, 9, 10, 10]
])

#Calcular la nota final de cada estudiante
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion_clase = calificaciones[:,3]

#nota final = 30% * examen1 + 30% * examen2 + 30% * trabajo final + 10% participacion clase
nota_final = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion_clase * 0.1

#imprimimos la nota final de cada estudiante

for i in range(len(nota_final)):
    print("La nota final del estudiante", i+1, "es:", np.round(nota_final[i],2))