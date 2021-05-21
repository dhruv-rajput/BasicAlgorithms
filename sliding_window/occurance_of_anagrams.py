#count occurance of anagrams in string

from collections import Counter
S = "aabaabaa"
ptr = "aaba"
k=len(ptr)
i=0
j=0
answer = 0
map = Counter(ptr) #count occurance of each alphabet in pattern.
count = len(map)
while(j<len(S)):
	if(S[j] in map):
		map[S[j]] -= 1   
		if(map[S[j]]) == 0:
			count -=1
	if(j-i+1<k):
		j = j+1
	elif(j-i+1==k):
		if count ==0: 	
			answer+=1
		if(S[i] in map):	
			map[S[i]] +=1
			if map[S[i]]==1:   
				count+=1
		i+=1
		j+=1
print(answer)




