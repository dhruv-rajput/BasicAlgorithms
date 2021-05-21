import math 
Coins = [10,2,3,5,7,12]
n = len(Coins)
S = 12
def Coin_Change(Coins,S,n):
	global t
	t = [[-1 for i in range(S + 1)] for j in range(n + 1)]
	for i in range(0,n+1):
		for j in range(0,S+1):
			if(j==0):
				t[i][j]=0
			if(i==0):
			    t[i][j]=math.inf-1
			if(i==1):
				if(j%Coins[0]==0):
					t[i][j]=j//Coins[0]
				else:
					t[i][j]=math.inf-1	

	for i in range(2,n+1):
		for j in range(1,S+1):	    
			if(Coins[i-1]<=j):
				t[i][j]=  min(1 + t[i][j-Coins[i-1]] , t[i-1][j])
			else:
				t[i][j] = t[i-1][j]
	return t[n][S]

print(Coin_Change(Coins,S,n))