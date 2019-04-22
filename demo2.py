"""
	Ejemplo de lenguaje Python
	autor @iancarlosortega
"""
import sys

#Ingresar valores mediante el terminal CMD

dato1 = sys.argv[1]
dato2 = sys.argv[2]

#Operaciones para calcular la suma y multiplicacion de los valores

suma = int(dato1)+int(dato2)
multi = int(dato1)*int(dato2)

#Mostrar en pantalla los resultados

print ("La suma es: %s" %suma)
print ("La multiplicacion es: %s" %multi)