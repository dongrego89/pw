class Publicacion(object):
	def __init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa):
		self.editor=editor
		self.pais=pais
		self.isbn=isbn
		self.anyo=anyo
		self.tapa=tapa
		self.paginas=paginas
	def getEditor(self):
		return self.editor
	def getPais(self):
		return self.pais
	def getIsbn(self):
		return self.isbn
	def getAnyo(self):
		return self.anyo
	def getPublicacion(self):
		print "Editorial: ",self.editor,"\nPais: ",self.pais,"\nISBN: ",self.isbn,"\nAnyo: ",self.anyo,"\nTapa: ",self.tapa," \nNo de Paginas: ",self.paginas

class Libro(Publicacion):
	def __init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa,autor,tipo,idioma):
		self.autor=autor
		self.tipo=tipo
		self.idioma=idioma
		Publicacion.__init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa)
	def getAutor(self):
		return self.autor
	def getTipo(self):
		return self.tipo
	def getIdioma(self):
		return self.idioma
	def getLibro(self):
		print "Autor: ",self.autor,"\nTipo: ",self.tipo,"\nIdioma: ",self.idioma
	
class Comic(Publicacion):
	def __init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa,autor,coleccion,idioma):
		self.autor=autor
		self.coleccion=coleccion
		self.idioma=idioma
		Publicacion.__init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa)
	def getAutor(self):
		return self.autor
	def getColeccion(self):
		return self.coleccion
	def getIdioma(self):
		return self.idioma
	def getComic(self):
		print "Autor: ",self.autor,"\nColeccion: ",self.coleccion,"\nIdioma: ",self.idioma

