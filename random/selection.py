def selection_sort(l):
	for i in range(0,len(l)): 
		minIndex = i
		for j in range(i+1,len(l)):
			if(l[j]<l[minIndex]):
				minIndex = j
		l[i], l[minIndex] = l[minIndex], l[i]
	return l	
l = [5,7,9,0,4,6,2,7,2,8,10,3,4,5,6]
array=selection_sort(l)
print(*array)