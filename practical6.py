class Sort:
	
	def bubble_sort(self,list):
		
		for i in range(0,len(list)-1):
			
			for j in range(0,len(list)-1-i):
				if list[j] > list[j+1]:
					list[j] , list[j+1] = list[j+1] , list[j]
					
				else:
					list[j]
		return list
			
	def insertionSort(self,arr):
		
		for i in range(1, len(arr)): 
		
			key = arr[i] 
			j = i-1
			
			while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
			arr[j+1] = key 
		return arr
		
	def selectionSort(self,arr):
		size = len(arr)
		for i in range(size-1):
			value = arr[i]
			j =i-1
			
		while j>=0 and value<arr[j]:
			arr[j+1]=arr[j]
			j -=1
		arr[j+1] = value
		return arr
			
	
obj = Sort()
list=[23,6,54,9,85]
print(list)

choice=input("enter type of search B for bubble sort ,I for insertion sort and S for selection sort")
if choice=="B":
	print(obj.bubble_sort(list))
	
elif choice=="I":
	print(obj.insertionSort(list))
	
elif choice=="S":
	print(obj.selectionSort(list))
	
else:
	print("make correct choice B,I,S")