x= "AGBCBA"
y= x[::-1]
n= len(x)
m= len(y)
t = [[0 for i in range(m + 1)] for j in range(n + 1)]

def minimum_deletion_to_palindrome(x,y,n,m):
	for i in range(1,n+1):
		for j in range(1,m+1):
			if(x[i-1]==y[j-1]):
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i-1][j],t[i][j -1])
	return t[n][m]

answer = minimum_deletion_to_palindrome(x,y,n,m)
print(n - answer)		 	
