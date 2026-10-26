'''
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. 
Para  ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.
(Pista 1) Tu array de entrada podría ser algo como esto, con datos de temperatura,
humedad, presión y mes del año:

'''

import numpy as np

clima = np.array([
#Temperatura, humedad, presión, mes
[20,70,1009,1],
[21,60,1011,1],
[22,40,1010,1],
[18,75,1012,2],
[21,60,1008,3],
[22,65,1008,3],
[25,60,1010,4],
[27,49,1007,5],
[29,50,1007,5],
[28,51,1007,5],
[30,45,1005,6],
[10,30,1005,6],
[32,40,1002,7],
[33,35,1001,8],
[31,45,1003,9],
[30,42,1001,9],
[29,42,1002,9],
[35,43,1001,9],
[28,50,1006,10],
[25,60,1010,11],
[27,59,1012,11],
[24,58,1011,11],
[22,70,1011,12]

])

meses = clima[:,-1]
print("Estos son todos los meses de la lista: ",meses)
print("-----")

temp_medias = np.zeros(12)

for mes in range(1,13):
    temp = clima[meses == mes]
    temp_medias[mes-1] = np.mean(temp[:,0])
print("La temperatura media es\n:",temp_medias)

hum_medias = np.zeros(12)

for mes in range(1,13):
    hum = clima[meses == mes]
    hum_medias[mes-1] = np.mean(hum[:,1])
print("Esta es la humedad media:\n ",hum_medias)

presion_medias = np.zeros(12)

for mes in range(1,13):
    presion = clima[meses == mes]
    presion_medias[mes-1] = np.mean(presion[:,2])
print("Esta es la presión atmosférica media:\n ",presion_medias)