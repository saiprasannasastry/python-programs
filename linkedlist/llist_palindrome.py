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

	def check_palindrome(self):
		temp=self.head
		list1=[]
		while temp:
			list1.append(temp.data)
			temp=temp.next
		s=list1[::-1]
		if s==list1:
			return True
		return False

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()
	for i in range(1,3):
		llist.push(i)

	llist.push(2)
	llist.push(1)
	llist.print()
	print()
	print(llist.check_palindrome())
