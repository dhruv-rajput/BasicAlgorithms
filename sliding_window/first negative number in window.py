l = [2,-1,7,5,9,6,-8,-6,9,1]
k=3
i=0
j=0
t = []
while(j<len(l)):
	if(l[j]<0):
		t.append(l[j])  #add all negative values
	if(j-i+1<k):
		j = j+1
	elif(j-i+1==k):
		if len(t)>0:
			print(t[0],end= " ") #if array is not empty print first value
		else:
			print(0,end=" ")
		if l[i]<0:
			t.pop(0) #if -ve found in main array delete from array of -ve values
		i = i + 1
		j = j + 1