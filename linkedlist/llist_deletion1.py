# delete the given position

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


	def delete_pos(self,position):
		if self.head is None:
			return
		temp=self.head

		if position==0:
			self.head=temp.next
			temp=None
			return

		for i in range(position-1):
			temp=temp.next
			if temp is None:
				break

		if temp.next is None:
			return

		if temp is None:
			return

		next=temp.next.next
		temp.next =None
		temp.next=next

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next
	

if __name__=='__main__':
	llist=linkedlist()
	llist.push(None)
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)
	

	llist.print()
	llist.delete_pos(3)
	print ()
	llist.print()
