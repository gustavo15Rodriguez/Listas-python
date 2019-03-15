#-*-coding:utf-8-*-

'''32. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar
cuántos números de los almacenados en la lista terminan en el mismo dígito que el último
valor leído.'''

try:
	lista = []


	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	num2 = int(raw_input("Digite el numero a evaluar: "))
	
	cont = 0
	for j in range(len(lista)):
		if lista[j]%10 == num2%10:
				cont+=1 

	print "De los numeros almacenados en la lista,%d numero(s) terminan en el ultimo digito del numero evaluado."%cont

except ValueError:
	print "Error..."