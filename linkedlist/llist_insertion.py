class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	def __init__(self):
		self.head=None
#insert at begining
	def insert(self,new_data):
		new_node=Node(new_data)

		new_node.next=self.head
		self.head=new_node

	def insert_after(self,prev_data,new_data):
		if prev_data is None:
			print('no new data is given')
			return
		new_node=Node(new_data)

		new_node.next=prev_data.next

		prev_data.next=new_node

	def add_last(self,new_data):

		new_node =Node(new_data)

		if self.head is None: 
			self.head = new_node 
			return
		last=self.head
		while(last.next):
			last=last.next

		last.next=new_node

	def printlist(self):
		temp=self.head
		while(temp):
			print (temp.data)
			temp=temp.next

if __name__=='__main__':
	list1=Linkedlist()
	'''
	list1.head=Node(1)
	second=Node(2)
	third=Node(3)

	list1.head.next=second
	second.next=third
    '''

	list1.add_last(6)
	list1.insert(4)
	list1.printlist()


