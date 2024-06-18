import matplotlib.pyplot as plt

anios = ['2021', '2022', "2023"] #Años
grupo_A = [18, 17, 15]  # Porcentajes para el grupo A en cada año
grupo_B = [32, 33, 34]  # Porcentajes para el grupo B en cada año
grupo_C = [28, 30, 30]  # Porcentajes para el grupo C en cada año
grupo_D = [12, 12, 13]  # Porcentajes para el grupo D en cada año
grupo_E = [10, 8, 8]  # Porcentajes para el grupo F en cada año

# Verificar que cada conjunto de datos sume 100%
for i in range(len(anios)):
    total_porcentaje = grupo_A[i] + grupo_B[i] + grupo_C[i] + grupo_D[i] + grupo_E[i]
    assert total_porcentaje == 100, f"La suma de porcentajes para el año {anios[i]} no es 100%"

# Crear el gráfico de barras apiladas
plt.figure(figsize=(10, 5))  # Tamaño opcional para la figura (ancho, alto)

# Barras para cada grupo de personas
plt.bar(anios, grupo_A, label='18 a 25')
plt.bar(anios, grupo_B, bottom=grupo_A, label='26 a 40')
plt.bar(anios, grupo_C, bottom=[grupo_A[j] + grupo_B[j] for j in range(len(grupo_A))], label='41 a 55')
plt.bar(anios, grupo_D, bottom=[grupo_A[j] + grupo_B[j] + grupo_C[j] for j in range(len(grupo_A))], label='56 a 65')
plt.bar(anios, grupo_E, bottom=[grupo_A[j] + grupo_B[j] + grupo_C[j] + grupo_D[j] for j in range(len(grupo_A))], label='Más de 65')

# Personalizar el gráfico
plt.xlabel('Años')   # Etiqueta del eje x
plt.ylabel('Porcentaje')      # Etiqueta del eje y
plt.title('Edad de los consumidores online en Chile')  # Título del gráfico
plt.ylim(0, 100)  # Ajustar el rango del eje y de 0 a 100%
plt.legend()  # Mostrar leyenda

# Mostrar el gráfico
plt.show()
