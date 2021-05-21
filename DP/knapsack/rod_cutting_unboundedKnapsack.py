length=[1,2,3,4,5,6,7,8]
Price=[1,5,8,9,10,17,17,20]
N = 8
n=len(length)
def rodCutting(length,Price,N,n):
	t = [[0 for i in range(N + 1)] for j in range(n + 1)]
	for i in range(1,n+1):
		for j in range(1,N+1):
			if(length[i-1]<=j):
				t[i][j]= max(Price[i-1]+t[i][j-length[i-1]],t[i-1][j])
			else:
				t[i][j] = t[i-1][j]
	return t[n][N]
	
answer = rodCutting(length,Price,N,n)
print(answer)