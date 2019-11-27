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

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

	def get_len(self):
		temp=self.head
		count =0
		while (temp):
			count+=1
			temp=temp.next

		return count

	def get_node(self,pos):
		temp=self.head
		len1=self.get_len()-1
		if pos==0:
		 	print()
		 	print(temp.data)
		if pos>0 and pos <=len1:
			for i in range(1,pos+1):

				temp=temp.next
				if i ==pos:
					print()
					print(temp.data)
					break
		else:
			print()
			print('no element corresponds to that position')

if __name__=='__main__':
	llist=Linkedlist()
	for i in range(6,11):
		llist.push(i)

	llist.print()
	llist.get_node(6)
	#print(llist.get_len())


#metod two
# def get_ele(self,pos):
# 	curr =self.head
# 	count=0
# 	while(curr):
# 		if count==pos:
# 			return curr.data
# 		count+=1
# 		curr=curr.next