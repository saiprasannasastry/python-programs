#find the key in an array

# def find_key(arr,key):
# 	for i,j in enumerate(arr):
# 		if j==key:
# 			return i

# arr=[1,4,5,6,7,8]
# key = 4

# print(find_key(arr,key))

arr=[1,4,5,6,6,8]
key = 6

for i in range(1,len(arr)):
	if key==arr[i]:
		print (i)
else:
	print("not found ")

