w=[10,20,30]
v=[60,100,120]
W= 50
n=len(w)
def knapsack(w,v,W,n):
	t = [[0 for i in range(W + 1)] for j in range(n + 1)]
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(w[i-1]<=j):
				t[i][j]= max(v[i-1]+t[i-1][j-w[i-1]],t[i-1][j])
			else:
				t[i][j] = t[i-1][j]
	return t[n][W]
	
answer = knapsack(w,v,W,len(w))
print(answer) 	
