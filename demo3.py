"""
	Ejemplo de lenguaje Python
	autor @iancarlosortega
"""
#Pedir al usuario el ingreso de los valores mediante teclado
print ("Ingrese el primer valor:")
valor1 = input()
print ("Ingrese el segundo valor:")
valor2 = input()

#Operaciones para calcular la suma y resto de los valores ingresados
suma = int(valor1) + int(valor2)
multi = int(valor1) * int(valor2)

#Mostrar en pantalla los resultados
print ("La suma es: %s \nLa multiplicacion es: %s" % (suma , multi))
