#Definiendo variables de los empleados
#Empleado 1
salario1 = int(3000000)
cargoempleado1 = ("directivo")
niveldedesempeño1 = ("alto")
#Empleado 2
salario2 = int(2500000)
cargoempleado2 = ("directivo")
niveldedesempeño2 = ("medio")
#Empleado 3
salario3 = int(1300000)
cargoempleado3 = ("auxiliar")
niveldedesempeño3 = ("bajo")
#Empleado 4
salario4 = int(1750000)
cargoempleado4 = ("operativo")
niveldedesempeño4 = ("medio")

#Entrada
print("Empleado 1")
print(f"Salario base mensual: ${salario1}")
print(f"Cargo empleado: {cargoempleado1.capitalize()}")
print(f"Nivel de desempeño: {niveldedesempeño1.capitalize()}")
print("Empleado 2")
print(f"Salario base mensual: ${salario2}")
print(f"Cargo empleado: {cargoempleado2.upper()}")
print(f"Nivel de desempeño: {niveldedesempeño2.capitalize()}")
print("Empleado 3")
print(f"Salario base mensual: ${salario3}")
print(f"Cargo empleado: {cargoempleado3.capitalize()}")
print(f"Nivel de desempeño: {niveldedesempeño3.capitalize()}")
print("Empleado 4")
print(f"Salario base mensual: ${salario4}")
print(f"Cargo empleado: {cargoempleado4.capitalize()}")
print(f"Nivel de desempeño: {niveldedesempeño4.upper()}")
#Salidas
# Directivos
porcentajead = 0.20
bonificacion1 = int(salario1 * porcentajead)
t1 = int(salario1 + bonificacion1)
print("")
print("------Resumen del Pago------")
print(f"Cargo: {cargoempleado1.capitalize()}")
print(f"Nivel de Desempeño: {niveldedesempeño1.capitalize()}")
print(f"Salario: ${salario1}")
print(f"Bonificacion: ${bonificacion1}")
print(f"Total a Recibir: ${t1}")
print("----------------------------")
print("")

porcentajemd = 0.10
bonificacion2 = int(salario2 * porcentajemd)
t2 = int(salario2 + bonificacion2)
print("------Resumen del Pago------")
print(f"Cargo: {cargoempleado2.capitalize()}")
print(f"Nivel de Desempeño: {niveldedesempeño2.capitalize()}")
print(f"Salario: ${salario2}")
print(f"Bonificacion: ${bonificacion2}")
print(f"Total a Recibir: ${t2}")
print("----------------------------")
print("")

# Otros
porcentajeau = 0
bonificacion3 = int(salario3 * porcentajeau)
t3 = int(salario3 + bonificacion3)
print("------Resumen del Pago------")
print(f"Cargo: {cargoempleado3.capitalize()}")
print(f"Nivel de Desempeño: {niveldedesempeño3.capitalize()}")
print(f"Salario: ${salario3}")
print(f"Bonificacion: ${bonificacion3}")
print(f"Total a Recibir: ${t3}")
print("----------------------------")
print("")

#operativos
porcentajemp = 0.05
bonificacion4 = int(salario4 * porcentajemp)
t4 = int(salario4 + bonificacion4)
print("------Resumen del Pago------")
print(f"Cargo: {cargoempleado4.capitalize()}")
print(f"Nivel de Desempeño: {niveldedesempeño4.capitalize()}")
print(f"Salario: ${salario4}")
print(f"Bonificacion: ${bonificacion4}")
print(f"Total a Recibir: ${t4} ")
print("----------------------------")



