"""
	Ejemplo de lenguaje Python
	autor @iancarlosortega
"""
import sys

#Ingresar valores mediante el terminal CMD

variable = sys.argv[0]
dato1 = sys.argv[1]
dato2 = sys.argv[2]
dato3 = sys.argv[3]

#Mostrar en pantalla los valores

print ("Variable argv[0]:   %s" % variable)
print ("Variable argv[1]:   %s" % dato1)
print ("Variable argv[2]:   %s" % dato2)
print ("Variable argv[3]:   %s" % dato3)
