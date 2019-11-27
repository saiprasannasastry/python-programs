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

	def reverse(self):
		#import pdb;pdb.set_trace()
		prev = None
		current = self.head 
		while(current is not None): 
			next = current.next
			current.next = prev 
			prev = current 
			current = next
		self.head = prev 

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

if __name__=='__main__':
	llist=Linkedlist()
	for i in range(6,11):
		llist.push(i)

	llist.print()
	llist.reverse()
	print()
	llist.print()