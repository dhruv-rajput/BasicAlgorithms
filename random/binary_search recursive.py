def binary_recursive(arr,l,r,key):
	if r>=l: 
		mid = l+(r-l)//2
		if arr[mid]==key: 
			return mid 
		elif arr[mid] >key: 
			return binary_recursive(arr, l, mid-1, key)
		else: 
			return binary_recursive(arr, mid + 1, r, key) 
	else: 
		return -1	
arr=[1,2,4,6,8,10,12,16,19,21]
result = binary_recursive(arr,0,len(arr)-1,3)
if(result==-1):
	print("Not Found")
else:
    print("Element Found at "+str(result+1))        	