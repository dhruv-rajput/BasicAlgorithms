def nsl(arr,n):
    ans=[]
    stack=[]
    i=0
    while i<n:  
        if len(stack)==0:
            ans.append(-1)
            
        elif len(stack)>0 and stack[0][0]<arr[i]:   
            ans.append(stack[0][1])
            
        elif len(stack)>0 and stack[0][0]>=arr[i]:
            while len(stack)>0 and stack[0][0]>=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0][1])
                
        stack.insert(0,(arr[i],i))   
        i+=1  
            
    return(ans)



def nsr(arr,n):
    ans=[]
    stack=[]
    
    i=n-1
    while i>=0:  
        if len(stack)==0:
            ans.append(n)
            
        elif len(stack)>0 and stack[0][0]<arr[i]:   
            ans.append(stack[0][1])
            
        elif len(stack)>0 and stack[0][0]>=arr[i]:
            while len(stack)>0 and stack[0][0]>=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                ans.append(n)
            else:
                ans.append(stack[0][1])
                
        stack.insert(0,(arr[i],i))   
        i-=1  
            
    return(ans[::-1])

arr=[6,2,5,4,5,1,6]
n=len(arr)
nsl=nsl(arr,n)
nsr=nsr(arr,n)
l=[]
for i in range(n):
    l.append(arr[i]*(nsr[i]-nsl[i]-1))
print(max(l))

