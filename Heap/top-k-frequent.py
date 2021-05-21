import heapq

l=[7,7,6,5,4,9,9,9,7,5,3,6,5,3,2,8,10,9]
hp=[]
k=3
dic={}
for i in l:
	if(i in dic):
		dic[i]+=1
	else:
	    dic[i]=1    

for i in dic:
	heapq.heappush(hp,(dic[i],i))
	if(len(hp)>k):
		heapq.heappop(hp)
while(len(hp)>0):
	print(heapq.heappop(hp)[1],end=" ")