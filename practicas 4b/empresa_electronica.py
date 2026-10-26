'''
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.
(Pista 1: Tu array de entrada puede tener la forma…)
(Pista 2: puede ser util investigar np.unique y np.argmax)

'''
import numpy as np

datos = np.array ([
# fecha producción, tipo de componente, lote, puntuación
['2022-01-01', 'Componente 1', 'Lote A', 80],
['2022-01-15', 'Componente 1','Lote B', 90],
['2022-02-01','Componente 2', 'Lote C', 85],
['2022-02-15','Componente 2','Lote D', 95],
['2022-03-01','Componente 1', 'Lote E', 75],
['2022-03-15', 'Componente 2', 'Lote F', 90]])


tipos_componente = datos[:,1]
componentes_unicos, conteo = np.unique(tipos_componente, return_counts=True)
calidad = datos[:,3].astype(float)
print("Estos son los valores de calidad de cada fabricación: ",calidad)
print("Estos son los valores únicos en ref. a los componentes en el array: ",componentes_unicos)
print("-----")
print("Las veces que se ha fabricado el ",componentes_unicos[0], "es ", conteo[0], "veces")
print("-----")
print("Las veces que se ha fabricado el ",componentes_unicos[1], "es ", conteo[1], "veces")
print("-----")

medias = np.zeros(len(componentes_unicos))

i = 0
for componentes in componentes_unicos:
    print(componentes)
    print(calidad[tipos_componente == componentes])
    medias[i] = np.mean(calidad[tipos_componente == componentes])
    i = i+1
print(medias)

print("---------------------")

mejor_media = np.argmax(medias)
producto_mas_calidad = componentes_unicos[mejor_media]
print("El producto con mejor media en la favbricación es ", producto_mas_calidad)

fechas = datos[:,0]
meses, conteo = np.unique([fecha[0:7]for fecha in fechas],return_counts=True)

for i in range(len(meses)):
    print("en el mes ", meses[i], "se fabricaron ", conteo[i])
    