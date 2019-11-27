import math
x=[5,5.5,25,100,36,9,4,7,8]

def find_sqares_in_array(x):
	n=len(x)-1
	list=[]
	for i in x:
			if math.sqrt(i)-int(math.sqrt(i))==0:
					list.append(i)
	print (list)

find_sqares_in_array(x)