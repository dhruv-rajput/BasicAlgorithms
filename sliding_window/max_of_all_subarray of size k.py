# to find maximum of all subarray of size k
l = [1,3,-1,-3,5,3,6,7]
k=3
i=0
j=0
c=0
max_list = [] #list to store maximums
while(j<len(l)):
	while(len(max_list)>0 and max_list[c]<l[j]): #remove all elements from front of list less than l[j]
		max_list.pop(c)
	max_list.append(l[j])
	if(j-i+1<k):
		j = j+1
	elif(j-i+1==k):
		print(max_list[0]) 
		if(max_list[0]==l[i]): #remove calculations of ith element by checking if it is present in front of max_list
			max_list.pop(0)
		i = i + 1	
		j = j + 1
