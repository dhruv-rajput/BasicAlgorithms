l = [2,9,7,5,9,6,3,6,9,1]
maxx=0
k=3
i=0
j=0
sum=0
while(j<len(l)):
	sum = sum + l[j]
	if(j-i+1<k):
		j = j+1
	elif(j-i+1==k):
		maxx = max(maxx,sum)
		sum = sum-l[i]
		i = i + 1	
		j = j + 1
print(max)