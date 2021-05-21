#Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

#Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

from collections import Counter
S = "TOTMTAPTAT"
ptr = "TTA"
i=0
j=0
map = Counter(ptr) #count occurance of each alphabet in pattern.
count = len(map)
while(j<len(S)):
	if(S[j] in map):
		map[S[j]]-=1
		if(map[S[j]]==0):
			count-=1
	if(count==0):	
		while(count==0):
			if(S[i] in map):
				map[S[i]]+=1
				if(map[S[i]]>0):
					count+=1
			i+=1	
		print(S[i-1:j+1])	
	j+=1


