#not fully done

# Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
# Output: true
# There is a pair (6, 10) with sum 16

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
# Output: true
# There is a pair (26, 9) with sum 35

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
# Output: false
# There is no pair with sum 45.

def sum_pair(arr,n,value):
	array=sorted(arr)
	smallest=0
	largest = n

	while smallest<largest and smallest >= 0 and largest < n:

		if array[smallest]+array[largest]==value:
			return 1
		elif array[smallest]+array[largest]<value:
			smallest +=1
		else:
			largest -=1
	return 0

arr=[11, 15, 26, 38, 9, 10]
value=41
n=len(arr)-1
if sum_pair(arr,value,n):
	print("sum exists")
else:
	print("no")

