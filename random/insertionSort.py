
def insertion_sort(l):
	for i in range(1 , len(l)):
		key = l[i]
		j = i-1
		while j>=0 and l[j]>key:
			l[j+1]=l[j]
			l[j]=key
			j=j-1
	return l

l = [5,7,9,0,4,6,2,7,2,8,10,3,4,5,6]
array=insertion_sort(l)
print(*array)
       