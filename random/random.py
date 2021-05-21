n = 7
a=3
b=2
x = [2,4,11,14,90,1000]
i=0
l=[]
k=0
while k<max(x):
	j=0
	while(True):
		if(k>=max(x)):
			break
		k = a**i + b**j
		l.append(k)
		j=j+1
	k = (l[-2])				
	i=i+1
for i in x:
	count=0
	for j in set(l):
		if(j<i):
			count+=1
	print(count)		


	

