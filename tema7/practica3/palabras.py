import random, string, time


def devPalabras(cadena):
	"Retorna una lista con cada linea del fichero que a su vez es una lista de palabras"
	fichero=open(cadena,"r")
	if fichero:	
		for i in fichero:
			lista=i.split()
		fichero.close()
		return lista
	else:
		return -1

def seleccionaElemento(lista):
	"Retorna un elemento aleatorio de una lista pasada por parametro"
	random.seed()
	return lista[random.randint(0,len(lista)-1)]

def introLetra():
	"Funcion que pide al usuario una letra asegurandose de que sea un caracter letra unitario"
	letra=raw_input("Introduce una letra: ")
	while bool(len(letra)>1) | bool(letra not in string.letters):
		letra=raw_input("Por favor, introduce una unica letra: ")
	return letra

def eliminaRepetido(nombre):
	listaDestino=[]
	fichero=open(nombre,"r")
	cadena=fichero.read()
	listaOriginal=cadena.replace("\n","").split()
	for i in listaOriginal:
		if i not in listaDestino:
			listaDestino.append(i)

	fichero.close()
	fichero=open(nombre,"w")
	fichero.write(" ".join(listaDestino))
	fichero.close()

def main():
	fallos=0
	aciertos=0
	comienzo=time.time()
	
	fichero=raw_input("Introduce el nombre del fichero fuente: ")
	lista=devPalabras(fichero)
	print "Lista de palabras: ",lista
	palabra=seleccionaElemento(lista)
	print "Palabra al azar: ",palabra
	pista=list(len(palabra)*"-")

	palabra=list(palabra)	

	while "-" in pista:
		letra=introLetra()
		if letra in palabra:
			while letra in palabra:
				
				pista[palabra.index(letra)]=letra
				palabra[palabra.index(letra)]="*"
			print "\n\tPista:",''.join(pista)
			aciertos+=1
		else:
			print "\n\tError."	
			fallos+=1
	print "Solucion:",''.join(pista)
	print "Has tenido un total de",aciertos,"aciertos y",fallos,"fallos\nJuego completado en",format(time.time()-comienzo,"4.4"),"segundos"
		

