x= "ABCDAF"
y= "ACBCF"
n= len(x)
m= len(y)
t = [[0 for i in range(m + 1)] for j in range(n + 1)]

def lcs(x,y,n,m):
	for i in range(1,n+1):
		for j in range(1,m+1):
			if(x[i-1]==y[j-1]):
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i-1][j],t[i][j -1])
		 	
def printing_lcs(t,n,m):
	ans = []
	i = n
	j = m
	while(i>0 and j>0):
		if(x[i-1]==y[j-1]):
			ans.append(x[i-1])
			i-=1
			j-=1
		else:
			if(t[i-1][j]>t[i][j-1]):
				i-=1
			else:
				j-=1
	return ans
lcs(x,y,n,m)
print(*printing_lcs(t,n,m)[::-1])


