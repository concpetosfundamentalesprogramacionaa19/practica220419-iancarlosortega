"""
	Problema 1 del laboratorio 1
	autor @iancarlosortega
"""
#Declaracion de las variables por teclado

x = input("Ingrese la variable x: \n")
y = input("Ingrese la variable y: \n")
z = input("Ingrese la variable z: \n")

#Operacion para encontrar el valor de m

m = (float(x)+(float(y)/float(z)))/(float(x)-(float(y)/float(z)))

#Mostrar en pantalla las variables y el resultado de m

print ("El valor de m, en base a las variables es: \nx = %s \n\ty = %s \n\t\tz= %s \nda como resultado: \n\t\t\tm = %.2f" % (x,y,z,m))