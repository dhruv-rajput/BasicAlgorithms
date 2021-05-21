import heapq

l=[7,6,5,3,2,8,10,9]
hp=[]
k=3
x=7
ans=[]
for i in l:
	heapq.heappush(hp,(-1*abs(7-i),i))
	if(len(hp)>k):
		heapq.heappop(hp)
for i in hp:
	print(i[1],end=" ")