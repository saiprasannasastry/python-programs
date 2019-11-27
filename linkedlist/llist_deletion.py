class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	def __init__(self):
		self.head=None

	def deletenode(self,key):
		temp=self.head

		if temp	is not None:
			if temp.data==key:
				self.head=temp.next
				temp= None
				return
		while temp is not None:
			if temp.data==key:
				break
			prev=temp
			temp=temp.next

		if temp==None:
			return

		prev.next=temp.next

		temp=None

	def printlist(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

if __name__=='__main__':
	llist=Linkedlist()
	llist.head=Node(1)
	second=Node(2)
	third=Node(3)
	fourth=Node(4)
	fifth=Node(5)

	llist.head.next=second
	second.next=third
	third.next=fourth
	fourth.next=fifth


	llist.printlist()
	llist.deletenode(3)
	print()
	llist.printlist()
