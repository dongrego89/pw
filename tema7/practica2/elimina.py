def rellenaLista(lista,num):
	for i in range(0,num):
		lista.append(raw_input("Introduce un elemento: "))
	return lista
		
def borraPares(lista):
	for i in lista:
		if type(i)==int:
			if i%2==0:
				lista.remove(i)
