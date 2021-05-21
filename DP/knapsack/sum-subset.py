w=[1,5,11,5]
S= 10
n=len(w)
t = [[-1 for i in range(S + 1)] for j in range(n + 1)]
def sum_subset(w,S,n):
	for i in range(0,n+1):
		for j in range(0,S+1):
			if(i==0):
				t[i][j]=False
			if(j==0):
			    t[i][j]=True	
	for i in range(1,n+1):
		for j in range(1,S+1):	    
			if(w[i-1]<=j):
				t[i][j]= (t[i-1][j-w[i-1]] or t[i-1][j])
			else:
				t[i][j] = t[i-1][j]
	return t[n][S]
	
answer = sum_subset(w,S,len(w))
print(answer) 	

