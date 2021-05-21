def binary_iterative(arr,key):
	l=0
	r=len(arr)-1
	while(l<=r):
		mid = l+(r-l)//2
		if(arr[mid]==key):
			return mid
		elif(arr[mid]<key):
			l = mid+1
		else:
			r = mid-1
	return -1		

arr=[1,2,4,6,8,10,12,16,19,21]
result = binary_iterative(arr,21)
if(result==-1):
	print("Not Found")
else:
    print("Element Found at "+str(result+1))	