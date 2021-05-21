x= "AGGTABABDNS"
y= "GXTXAYBNAIDSMAN"
n= len(x)
m= len(y)

def lcs(x,y,n,m):
	t = [[-1 for i in range(m+1)] for j in range(n+1)]

	if(n==0 or m==0):
		return 0
	if(t[n][m]!=-1):
	    return t[n][m] 	
	if(x[n-1]==y[m-1]):
	    t[n][m] = 1 + lcs(x,y,n-1,m-1)
	    return t[n][m]

	else:
	    t[n][m] =  max(lcs(x,y,n-1,m),lcs(x,y,n,m-1))
	    return t[n][m]    	


answer = lcs(x,y,n,m)
print(answer)