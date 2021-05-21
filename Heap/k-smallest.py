import heapq

l=[7,3,5,4,8,1,9,2]
hp=[]
k=3
for i in l:
	heapq.heappush(hp,-1*i)
	if(len(hp)>k):
		heapq.heappop(hp)
while(len(hp)>0):
    print(-1*(heapq.heappop(hp)),end=" ")		
print(heapq.nsmallest(3, l))    