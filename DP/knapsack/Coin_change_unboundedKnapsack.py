Coins = [1,2,3]
n = len(Coins)
S = 5
def Coin_Change(Coin,S,n):
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
			if(Coins[i-1]<=j):
				t[i][j]=  t[i][j-Coins[i-1]] + t[i-1][j]
			else:
				t[i][j] = t[i-1][j]
	return t[n][S]

print(Coin_Change(Coins,S,n))