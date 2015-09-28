class Publicacion():
	def __init__(self,editor,direccion,pais,isbn,anyo,paginas,tapa):
		self.editor=editor
		self.pais=pais
		self.isbn=isbn
		self.anyo=anyo
	def getEditor(self):
		return self.editor
	def getPais(self):
		return self.pais
	def getIsbn(self):
		return self.isbn
	def getAnyo(self):
		return self.anyo
	def getDatos(self):
		print "Editorial: ",self.editor,"\nPais: ",self.pais,"\nISBN: ",self.isbn,"\nAnyo: ",self.anyio,"\nTapa: ",self.tapa," \nNo de Paginas: ",paginas

class Libro(Publicacion):
	def __init__(self,autor,tipo,pais,idioma):
		self.autor=autor
		self.tipo=tipo
		self.pais=pais
		self.idioma=idioma

	def getAutor(self):
		return self.autor
	def getTipo(self):
		return self.tipo
	def getPais(self):
		return self.pais
	def getIdioma(self):
		return self.idioma
	
class Comic(Publicacion):
	def __init__(self,autor,coleccion,pais,idioma):
		self.autor=autor
		self.coleccion=coleccion
		self.pais=pais
		self.idioma=idioma
#preguntar como inicializar al padre super
	def getAutor(self):
		return self.autor
	def getColeccion(self):
		return self.coleccion
	def getPais(self):
		return self.pais
	def getIdioma(self):
		return self.idioma

