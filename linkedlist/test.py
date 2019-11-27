#Hackerrank sol1
# def sort(data):
#     count =0
#     for i in range(len(data)):
#         for j in range(len(data)-i-1):
#             if data[j]-j >2:
#                 return False
#             if data[j] >data[j+1]:
#                 data[j],data[j+1]= data[j+1],data[j]
#                 count+=1
#     return count
# data=[1,3,2,5,4]
# print (sort(data))
# data=[1,5,3,4,2]
# print (sort(data))

#SORT O'S AND 1'S
# def sort(data):
#     n=len(data)
#     count=0
#     for i in range(n):
#         if data[i]==0:
#             count+=1
#     list1=[]
#     for i in range (count):
#         list1.append(0)
#     for i in range (n-count):
#         list1.append(1)
#     print(list1)

# data=[0,1,1,0,1,1,1,0]
# sort(data)

#fIND MISSING NUMBER IN ap
#
# def find_missing(arr):
#     n=len(arr)
#     if n>=2:
#         d=arr[1]-arr[0]
#     for i in range(n):
#         if arr[i+1]-arr[i] ==d:
#             continue
#         else:
#             return arr[i+1]-d
# arr=[2,4,8,10]
# print(find_missing(arr))

def minSwaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans


# Driver Code
arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))
