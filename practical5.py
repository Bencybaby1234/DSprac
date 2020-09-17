class search:
	
	def linear_search(self,list,element):
		
		for i in range(0,len(list)):
			if element == list[i]:
				return i
				
			else:
				return -1
				
	def binary_search(self,arr,element):
		start=0
		end = len(arr) 
		mid = 0
		
		while(start<=end):
			
			mid = (start+end)//2
			
			if element==arr[mid]:
				return mid
				
			elif element>arr[mid]:
				start = mid+1
				
			else:
				end = mid-1
				
		return -1
				
				
		
		
choice = input(" enter your choice of search press B for binary search and L for linear search : ")

list=[2,6,9,15,19,20]
print(list)
element = int(input("enter search element :"))

obj1 = search()
if choice=='B':
	result = obj1.binary_search(list,element)
	
elif choice=='L':
	print(obj1.linear_search(list,element))
	
else:
	print(" invalid option")
	
if result != -1: 

    print("Element is present at index", str(result)) 

else: 

    print("Element is not present in array") 
