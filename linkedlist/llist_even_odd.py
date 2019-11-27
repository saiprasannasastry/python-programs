#not done


class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	def __init__(self):
		self.head=None

	def printlist(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

	def move_even_odd(self):
		temp=self.head

		if temp.data%2==0:
			temp=temp.next
		else:
			prev=temp
			self.head=temp.next
			prev.next=temp.next



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
	llist.move_even_odd()
	print()
	llist.printlist()