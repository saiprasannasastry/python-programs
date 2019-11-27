class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node=node(data)
		new_node.next=self.head
		self.head=new_node

	def deleteall(self):
		current=self.head

		while(current):
			prev= current.next
			del current.data

			current = prev

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

if __name__=='__main__':
	llist=linkedlist()
	for i in range(5):
		llist.push(i)

	llist.print()
	llist.deleteall()
	llist.print()



