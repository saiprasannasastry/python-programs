class Node:
    def __init__(self,data):
        self.data=data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head =None
    
    def push(self,data):
        new_node= Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
    
    def rotate(self,n):
        temp=self.head
        list1=[]
        for i in range(n):
            temp=temp.next
        kthNode=temp

        while(temp.next is not None): 
            temp = temp.next
        #print(temp.data)
        temp.next=self.head
        self.head=kthNode.next
        kthNode.next = None

if __name__=='__main__':
    llist=LinkedList()
    for i in range(1,8):
        llist.push(i)
    llist.print_list()
    llist.rotate(3)
    print()
    llist.print_list()