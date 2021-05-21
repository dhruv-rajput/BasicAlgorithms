l = [5,7,9,0,4,6,2,7,2,8,10,3,4,5,6]
for t in range(0,len(l)):
 for i in range(1,len(l)-t):
 	if(l[i-1]>l[i]):
 		l[i-1],l[i]=l[i],l[i-1]
 print(l)
	
