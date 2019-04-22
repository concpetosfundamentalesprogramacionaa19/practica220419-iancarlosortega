"""
	Problema 1 del laboratorio 1
	autor @iancarlosortega
"""
#Declaracion de variables e ingreso por teclado

horas = 100
costo = input("Por favor ingrese el costo por hora oficial: \n")

#Operaciones para calcular el sueldo mensual del trabajador

total = float(horas) * float(costo)
descuento = float (total) * 0.1

#Mostrar en pantalla el sueldo

print ("El sueldo mensual del trabajador es: %.1f" % descuento)