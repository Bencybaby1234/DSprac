# Python program to insert in a sorted list 

  
# Node class  

class Node: 

  

    # Constructor to initialize the node object 

    def __init__(self, data): 

        self.data = data 

        self.next = None

  

class LinkedList: 
	# Function to initialize head 

    def __init__(self): 

        self.head = None

  

    def sortedInsert(self, new_node): 
		# Special case for the empty linked list  

        if self.head is None: 

            new_node.next = self.head 

            self.head = new_node 

 	 # Special case for head at end 

        elif self.head.data >= new_node.data: 

            new_node.next = self.head 

            self.head = new_node 

  

        else : 
	# Locate the node before the point of insertion 

            current = self.head 

            while(current.next is not None and

                 current.next.data < new_node.data): 

                current = current.next

              

            new_node.next = current.next

            current.next = new_node 

  

    # Function to insert a new node at the beginning 

    def push(self, new_data): 

        new_node = Node(new_data) 

        new_node.next = self.head 

        self.head = new_node 

  

    # Utility function to print it the linked LinkedList 

    def printList(self): 

        temp = self.head 

        while(temp): 

            print (temp.data) 

            temp = temp.next
 
    def find_index(self, key):
        
        return self.find_index_helper(key, 0, self.head)
 
    def find_index_helper(self, key, start, node):
        if node is None:
            return -1
 
        if node.data == key:
            return start
            
        else:
            return self.find_index_helper(key, start + 1, node.next)
            
	def delete_llist(self,element):
	           
            
def reverse_llist(llist):
    before = None
    current = llist.head
    if current is None:
        return
    after = current.next
    while after:
        current.next = before
        before = current
        current = after
        after = after.next
    current.next = before
    llist.head = current
    
llist = LinkedList() 

new_node = Node(5) 
llist.sortedInsert(new_node) 

new_node = Node(10) 
llist.sortedInsert(new_node) 

new_node = Node(7) 
llist.sortedInsert(new_node) 

new_node = Node(3) 
llist.sortedInsert(new_node) 

new_node = Node(1) 
llist.sortedInsert(new_node) 

new_node = Node(9) 
llist.sortedInsert(new_node) 

print ("Create Linked List")
llist.printList() 

print('The linked list: ', end = '')

print()
 
key = int(input('What data item would you like to search for? '))
index = llist.find_index(key)
if index == -1:
    print(str(key) + ' was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')
    
rev =reverse_llist(llist)
print(rev)
    

 

  