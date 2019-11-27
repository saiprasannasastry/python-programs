class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node= Node(data)
		new_node.next=self.head
		self.head=new_node

	def detectLoop(self): 
		slow = self.head 
		fast = self.head 
		flag=0
		while(slow and fast and fast.next): 
			if slow == fast and flag != 0: 
                  
                # Means loop is confirmed in the  
                # Linked List. Now slow and fast  
                # are both at the same node which 
                # is part of the loop 
				count = 1
				slow = slow.next
				while(slow != fast): 
					slow = slow.next
					count += 1
				return count 
              
			slow = slow.next
			fast = fast.next.next
			flag = 1
		return 0 # No l


	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()
	for i in range(6,13):
		llist.push(i)

	llist.head.next.next.next.next=llist.head
	print(llist.detectLoop())
