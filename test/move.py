

def moce(x,n):
	# import pdb;pdb.set_trace()
	y=[]
	while len(y)<=2:
		for i in x:
			x.pop(i)
			# print(x)
			y.append(i)
	return y

x=[2,4,6,8,9]
n=2

print(moce(x,n))