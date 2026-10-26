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

import numpy as np


al1 = np.random.uniform(0,10.01, size=4)
alumno1 = np.round(al1,2)
print("Notas de Maria",alumno1)
valia = np.round([30,30,30,10])/100
valor_final1 = valia * alumno1
print("Valor en porcentaje de notas ",valor_final1)
suma_total1 = sum(valor_final1)
print("Nota definitiva Maria ",np.round(suma_total1,2))
print("---")

al2 = np.random.uniform(0,10.01, size=4)
alumno2 = np.round(al2,2)
print("Notas de Raúl ",alumno2)
valia = np.round([30,30,30,10])/100
valor_final2 = valia * alumno2
print("Valor en porcentaje de notas ",valor_final2)
suma_total2 = sum(valor_final2)
print("Nota definitiva Raúl ",np.round(suma_total2,2))
print("---")

al3 = np.random.uniform(0,10.01, size=4)
alumno3 = np.round(al3,2)
print("Notas de Nuria",alumno3)
valia = np.round([30,30,30,10])/100
valor_final3 = valia * alumno3
print("Valor en porcentaje",valor_final3)
suma_total3 = sum(valor_final3)
print("Nota definitiva Nuria ",np.round(suma_total3,2))
print("---")

al4 = np.random.uniform(0,10.01, size=4)
alumno4 = np.round(al4,2)
print("Notas de Alberto",alumno4)
valia = np.round([30,30,30,10])/100
valor_final4 = valia * alumno4
print("Valor en porcentaje ",valor_final4)
suma_total4 = sum(valor_final4)
print("Nota definitiva Alberto ",np.round(suma_total4,2))
print("---")

al5 = np.random.uniform(0,10.01, size=4)
alumno5 = np.round(al5,2)
print("Nota de Sandra", alumno5)
valia = np.round([30,30,30,10])/100
valor_final5 = valia * alumno5
print("Valor en porcentaje ",valor_final5)
suma_total5 = sum(valor_final5)
print("Nota definitiva Sandra ",np.round(suma_total5,2))
print("---")

array_alumnos = np.vstack((alumno1, alumno2, alumno3, alumno4, alumno5))
print("Estas son las notas de los alumnos \n",array_alumnos)

definitivo_global = []
definitivo_global.append(suma_total1)
definitivo_global.append(suma_total2)
definitivo_global.append(suma_total3)
definitivo_global.append(suma_total4)
definitivo_global.append(suma_total5)
listado_final = np.array(definitivo_global, dtype=float)
print("Notas final curso: ",np.round(listado_final, 2))