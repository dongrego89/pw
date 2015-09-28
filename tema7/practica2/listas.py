frase1=raw_input("Introduce la primera frase: ")
frase2=raw_input("Introduce la segunda frase: ")

frase1=frase1.split()
frase2=frase2.split()

for i in frase2:
	if i in frase1:
		frase1.remove(i)

print frase1
print frase2

def ordenaLista(lista,orden):
	if orden=="asc":
		return lista.sort()
	else:
		return lista.reverse()
