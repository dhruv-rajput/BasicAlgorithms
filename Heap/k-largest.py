import heapq

l=[7,3,5,4,8,1,9,2]
hp=[]
k=3
for i in l:
	heapq.heappush(hp,i)
	if(len(hp)>k):
		heapq.heappop(hp)
while(len(hp)>0):
    print(heapq.heappop(hp),end=" ")		
print(heapq.nlargest(k, l))