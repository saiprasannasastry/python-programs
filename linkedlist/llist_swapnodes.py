class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node =node(data)

		new_node.next=self.head
		self.head=new_node

	def get_len(self):
		temp=self.head
		count =0
		while (temp):
			count+=1
			temp=temp.next

		return count

	def swapNodes(self, x, y): 
  
		# Nothing to do if x and y are same 
		if x == y: 
			return 
  
        # Search for x (keep track of prevX and CurrX) 
		prevX = None
		currX = self.head 
		while currX != None and currX.data != x: 
			prevX = currX 
			currX = currX.next
  
		# Search for y (keep track of prevY and currY) 
		prevY = None
		currY = self.head 
		while currY != None and currY.data != y: 
			prevY = currY 
			currY = currY.next
  
		# If either x or y is not present, nothing to do 
		if currX == None or currY == None: 
			return 
		# If x is not head of linked list 
		if prevX != None: 
			prevX.next = currY 
		else: #make y the new head 
			self.head = currY 
  
        # If y is not head of linked list 
		if prevY != None: 
			prevY.next = currX 
		else: # make x the new head 
			self.head = currX 
  
        # Swap next pointers 
		temp = currX.next
		currX.next = currY.next
		currY.next = temp 
	def print(self):
		temp=self.head
		count=0
		while(temp):
			print(temp.data,end=' ')
			temp=temp.next

if __name__=='__main__':
	llist=linkedlist()
	for i in range(1,8):
		llist.push(i)

	llist.print()

	llist.swapNodes(1,2)
	print()
	llist.print()