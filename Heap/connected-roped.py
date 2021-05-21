import heapq
hp=[1,2,3,4,5]
heapq.heapify(hp)
cost=0
while len(hp)>=2:
	 first = heapq.heappop(hp)
	 second = heapq.heappop(hp) 
	 cost+=first+second
	 heapq.heappush(hp,first+second)
print(cost)     