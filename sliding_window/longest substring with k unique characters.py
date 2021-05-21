#Given a string you need to print the size of the longest possible substring that has exactly k unique characters.
S = 'aaaa'
i = 0
j = 0
k = 1
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