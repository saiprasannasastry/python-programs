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

	def get_len(self):
		temp=self.head
		count=0
		while temp:
			count+=1
			temp=temp.next
		return count

	def remove(self,pos):
		temp=self.head
		position=self.get_len()-pos
		if position<0:
			print()
			print('No element resides in that position')
		if position ==0:
			print()
			print(temp.data)
		for i in range(1,position+1):
				temp=temp.next
				if i==position:
					print()
					print(temp.data)


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
	llist.remove(6)
