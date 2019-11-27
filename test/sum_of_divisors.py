#sum of all factors
import math

def sumfactors(n):
	result=0
	for i in range(2,int((math.sqrt(n))+1)):
		if (n % i == 0) : 
  
            # if both divisors are same  
            # then add it only once 
            # else add both 
			if (i == (n/i)): 
				result = result + i 
			else: 
				result = result + (i + n//i) 
	return (result+n+1)

print (sumfactors(6))


