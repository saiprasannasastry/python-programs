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

	def removeDuplicates(self): 
		temp = self.head 
		if temp is None: 
			return
		while temp.next is not None: 
			if temp.data == temp.next.data: 
				new = temp.next.next
				temp.next = None
				temp.next = new 
			else: 
				temp = temp.next
		return self.head 
		#return self.head 


	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()


	llist.push(5)
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(2)
	llist.push(1)
	llist.print()
	print()
	llist.removeDuplicates()
	llist.print()