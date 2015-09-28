class Animal:
	def __init__(self,tipo,raza): #esto es el constructor
		self.tipo=tipo
		self.raza=raza


	def hablar(self,mensaje):
		print "Soy un",self.tipo,"de raza", self.raza, ":",mensaje

