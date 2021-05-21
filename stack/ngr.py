def ngr(arr,n):
    ans=[]
    stack=[]
    i=n-1
    while i>=0:  
        if len(stack)==0:
            ans.append(-1)
            
        elif len(stack)>0 and stack[0]>arr[i]:    
            ans.append(stack[0])
            
        elif len(stack)>0 and stack[0]<=arr[i]:
            while len(stack)>0 and stack[0]<=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0])
                
        stack.insert(0,arr[i])  
        i-=1  
            
    print(*ans[::-1])
arr=[100,80,60,70,60,75,85]
n=len(arr)
ngr(arr,n)
