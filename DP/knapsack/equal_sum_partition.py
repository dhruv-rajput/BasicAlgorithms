w=[1,5,11,5]
n=len(w)
def sum_subset(w,S,n):
	t = [[-1 for i in range(S + 1)] for j in range(n + 1)]
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

def equal_sum_partiton(w):	
	if(sum(w)%2!=0):
		return False
	else:
	    return sum_subset(w,sum(w)//2,len(w))

answer = equal_sum_partiton(w)
print(answer)