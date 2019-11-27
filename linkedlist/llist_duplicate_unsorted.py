#not completed
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

	def get_count(self):
		temp=self.head
		count=0
		while temp:
			count+=1
			temp=temp.next
		return count
	def remove_duplicates(self):
		temp=self.head
		position=self.get_count()
		list1=[]
		for element in range(0,position-1):
			list1.append(temp.data)
			prev=temp
			temp=temp.next
			if temp.data in list1:
				if temp.next is not None :
					if temp.next and temp.next.next not in list1:
						prev.next=temp.next.next

		print (list1)

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()

	#llist.push(2)
	llist.push(5)
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(2)
	llist.push(5)
	llist.push(1)
	llist.push(4)
	llist.push(2)
	llist.push(1)
	llist.print()
	print()
	llist.remove_duplicates()
	llist.print()
