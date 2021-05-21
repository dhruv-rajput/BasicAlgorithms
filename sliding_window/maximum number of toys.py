#John is at a toy store help him pick maximum number of toys. He can only select in a continuous manner and he can select only two types of toys.
S = 'abaccab'
i = 0
j = 0
k = 2
dic = {}
while(j<len(S)):
	dic[S[j]] = dic.get(S[j],0) + 1
	if(len(dic)<k):
		j+=1
	if(len(dic)==k):
		print(j-i+1)
		j+=1
	if(len(dic)>k):
	    while(len(dic)>k):
	    	dic[S[i]]-=1
	    	if(dic[S[i]]==0):
	    		dic.pop(S[i])
	    	i+=1
	    j+=1