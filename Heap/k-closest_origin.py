import heapq

l=[(1,3),(-2,2),(5,8),(0,1)]
hp=[]
k=2
for i in l:
	heapq.heappush(hp,(-1*(i[0]*i[0]+i[1]*i[1]),i))
	if(len(hp)>k):
		heapq.heappop(hp)
for i in hp:
	print(i[1],end=" ")