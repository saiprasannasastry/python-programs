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

	def detect_loop(self):
		s =set()

		temp=self.head
		#print(temp.data)
		while temp :
			#list1.append(temp.data)
			
			if temp in s:
				return True
			s.add(temp)
			temp=temp.next
		return False
# def detectLoop(self): 
#         slow_p = self.head 
#         fast_p = self.head 
#         while(slow_p and fast_p and fast_p.next): 
#             slow_p = slow_p.next
#             fast_p = fast_p.next.next
#             if slow_p == fast_p: 
#                 print "Found Loop"
#                 return 

	def print(self):
		temp=self.head
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next


if __name__=='__main__':
	llist=Linkedlist()
	for i in range(6,13):
		llist.push(i)

	llist.head.next.next.next=llist.head
	print(llist.detect_loop())