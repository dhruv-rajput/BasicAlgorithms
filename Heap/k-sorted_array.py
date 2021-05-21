import heapq

l=[6,5,3,2,8,10,9]
hp=[]
k=3
ans=[]
for i in l:
	heapq.heappush(hp, i)
	if(len(hp)>k):
		ans.append(heapq.heappop(hp))
while(len(hp)>0):
    ans.append(heapq.heappop(hp))
print(ans)    