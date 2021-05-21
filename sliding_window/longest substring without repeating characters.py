#Given a string s, find the length of the longest substring without repeating characters.
S = 'pwwkew'
i = 0
j = 0
k = 3 
dic = {}
while(j<len(S)):
	if(S[j] not in dic):
		dic[S[j]]=1
	else:
		dic[S[j]]+=1
	if(len(dic)==j-i+1):
		print(j-i+1)
		j+=1
	elif(len(dic)<j-i+1):
	    while(len(dic)<j-i+1):
	    	dic[S[i]]-=1
	    	if(dic[S[i]]==0):
	    		dic.pop(S[i])
	    	i+=1
	    j+=1