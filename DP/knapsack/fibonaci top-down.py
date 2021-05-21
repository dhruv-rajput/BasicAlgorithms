
n = 50
t=[0]*(n+1)
t[1]=1
def fibonaci(n):
	for i in range(2,n+1):
		t[i]=t[i-1]+t[i-2]

	return t[n]	
print(fibonaci(n))	