# print most occoured element count
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

	def get_occourance(self,data):
		temp=self.head
		count =0
		for i in range(0,self.get_len()):
			if temp.data==data:
				count+=1
			temp=temp.next
		return count

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()
	for i in range(1,6):
		llist.push(i)
	for i in range(2):
		llist.push(2)
	llist.push(3)
	llist.print()
	print()
	#print(llist.get_len())
	print(llist.get_occourance(2))
	print(llist.get_occourance(3))
	print(llist.get_occourance(0))