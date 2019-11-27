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

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

	def search(self,node):
		temp=self.head
		while (temp):
			if temp.data==node:
				print(' ')
				print('yes')
				break
			temp=temp.next
		else:
			print()
			print('no')



if __name__=='__main__':
	llist=Linkedlist()
	for i in range(6):
		llist.push(i)

	llist.print()
	llist.search(5)

