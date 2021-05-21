w=[10,20,30]
v=[60,100,120]
W= 50
n=len(w)
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsack(w,v,W,n):
	if(W==0 or n==0):
		return 0
	if(t[n][W] != -1):
	    return t[n][W]

	if(w[n-1]<=W):
	    t[n][W]=max(v[n-1]+knapsack(w,v,W-w[n-1],n-1),knapsack(w,v,W,n-1))
	    return t[n][W]
	elif(w[n-1]>W):
		t[n][W]= knapsack(w,v,W,n-1)  
		return t[n][W]   	


answer = knapsack(w,v,W,len(w))
print(answer) 