import sys

def divisible(n1,n2):
	return n1%n2==0

if len(sys.argv) == 3:
	if divisible(int(sys.argv[1]),int(sys.argv[2])):
		print "Es divisible"
	else:
		print "No es divisible"
else:
	num1=input("Introduce el dividendo: ")
	num2=input("Introduce el divisor: ")

	if divisible(num1,num2):
		print "Es divisible"
	else:
		print "No es divisible"
	
