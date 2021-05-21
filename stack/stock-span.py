def ngr(arr,n):
    ans=[]
    stack=[]
    
    i=0
    while i<n:  
        if len(stack)==0:
            ans.append(-1)
            
        elif len(stack)>0 and stack[0][0]>arr[i]:    
            ans.append(stack[0][1])
            
        elif len(stack)>0 and stack[0][0]<=arr[i]:
            while len(stack)>0 and stack[0][0]<=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0][1])
                
        stack.insert(0,(arr[i],i))   
        i+=1          
    for i in range(n):
        print(i-ans[i],end=" ")

arr=[100,80,60,70,60,75,85]
n=len(arr)
ngr(arr,n)