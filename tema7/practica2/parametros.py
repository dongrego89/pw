def estadisticas(palabras):
	minima=maxima=len(palabras[0])
	media=0
	retorno=[]
	for i in palabras:
		retorno.append(len(i))
		media=media+len(i)
		if(len(i)>maxima):
			maxima=len(i)
		if(len(i)<minima):
			minima=len(i)
	return (retorno,media/len(palabras),maxima,minima)
