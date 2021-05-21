w=[2,3,5,6,8,10]
n=len(w)
def sum_subset(w,S,n):
	global t
	t = [[-1 for i in range(S + 1)] for j in range(n + 1)]
	for i in range(0,n+1):
		for j in range(0,S+1):
			if(i==0):
				t[i][j]=0
			if(j==0):
			    t[i][j]=1	
	for i in range(1,n+1):
		for j in range(1,S+1):	    
			if(w[i-1]<=j):
				t[i][j]=  t[i-1][j-w[i-1]] + t[i-1][j]
			else:
				t[i][j] = t[i-1][j]
	return t[n][S]

print(sum_subset(w,10,len(w)))
