# lanzar python en consola para ver la version

print 3,"+",4,"=",3+4
print 3,"-",4,"=",3-4
print 3,"x",4,"=",3*4
print 12,"/",4,"=",12/4
print 2,"^",4,"=",2**4
print 4,"%",2,"=",4%2
print
print float(5)/2
print "perro","x",3,"=","perro "*3
cadena="Perro"
print cadena=="Perro"
print cadena=="Gato"
print cadena!="Perro"
import math

print "El seno de 0 es",math.sin(0)
print "La raiz cuadrada de 9 es",math.sqrt(9)
import rlcompleter, readline
readline.parse_and_bind("tab:complete")

def imprime(cadena):
    "Esta funcion imprime lo que le pases por parametro"
    print "Tengo que imprimir",cadena

    
