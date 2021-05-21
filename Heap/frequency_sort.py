import heapq

l=[1,1,1,3,2,2,4]
hp=[]
k=3
dic={}
for i in l:
	if(i in dic):
		dic[i]+=1
	else:
	    dic[i]=1    

for i in dic:
	heapq.heappush(hp,(-1*dic[i],i))
while(len(hp)>0):
	p=heapq.heappop(hp)
	for i in range(0,-1*p[0]):
		print(p[1],end=" ")