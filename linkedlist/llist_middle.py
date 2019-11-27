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

	def get_middle(self):
		temp=self.head
		remainder= self.get_len()%2
		middle=int(self.get_len()/2)
		if remainder==0:
			for i in range(0, middle+1):
				if i==middle:
					print()
					print(temp.data)
					break
				temp=temp.next
		else:
			middle = int(middle+0.5)
			for i in range(0, middle+1):
				if i==middle:
					print()
					print(temp.data)
					break
				temp=temp.next			


	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()
	for i in range(5,13):
		llist.push(i)

	llist.print()
	llist.get_middle()