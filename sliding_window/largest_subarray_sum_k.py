# variable size subarray
# to find largest subarray of sum k
# Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K. 

l = [5,6,5,7,5,7,1,3,2,1,2,1,5]
i = 0 
j = 0
k = 5 
sum = 0
while(j<len(l)):
	sum = sum + l[j]
	if(sum == k):
		print(j-i+1)
	if(sum > k):
		while(sum > k):
			sum = sum - l[i]
			i+=1
			if(sum == k):
				print(j-i+1)
	j+=1		
		