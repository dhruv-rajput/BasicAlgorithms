
n = 50
t=[-1]*(n+1)
def fibonaci(n):
	if(n==0 or n==1):
		return n
	if(t[n]!=-1):
	    return t[n] 	
	else:
		t[n] =  (fibonaci(n-1)+fibonaci(n-2))
		return t[n]  
print(fibonaci(n))