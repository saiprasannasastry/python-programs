class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node =node(data)

		new_node.next=self.head
		self.head=new_node

	def print(self):
		temp=self.head
		count=0
		while(temp):
			count +=1
			print(temp.data,end=' ')
			temp=temp.next
		print (' ')
		print (count)

if __name__=='__main__':
	llist=linkedlist()
	for i in range(1,5):
		llist.push(i)

	llist.print()