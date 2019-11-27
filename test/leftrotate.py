#rotate an array of size n d times
def leftrotate(arr,d,n):
    for i in range(d):
        leftrotateby1(arr,n)
    for i in range(n):
        print(arr[i],  end = " ")
def leftrotateby1(arr,n):
    tmp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1] =tmp

arr=[1,2,3,4,5]
leftrotate(arr,2,5)



