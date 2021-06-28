from random import randint

def isPrime(num):
	cont = 0
	i = 1

	for i in range(0, num):
		i+=1
		if (num%i == 0):
			cont+=1; 

	if cont == 2:
		return True;
	
	return False;


def getPrime():
   result = False;
   
   while result == False:
    	# You can modify limit to get random prime number
    	random = randint(0, 1000)
    	if isPrime(random):
    		result = random   
   
   return result;
