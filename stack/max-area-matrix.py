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

def MAH(arr,n):
    nsl1=0
    nsr1=0
    nsl1=nsl(arr,n)
    nsr1=nsr(arr,n)
    l=[]
    for i in range(n):
        l.append(arr[i]*(nsr1[i]-nsl1[i]-1))
    return(max(l))

arr = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
ans=[]

for i in range(0,len(arr)):
    if(i==0):
        ans.append(arr[0]) 
    else:
        temp=[]
        for j in range(0,len(arr[0])):
            if(arr[i][j]==0):
                temp.append(arr[i][j])
            else:   
                temp.append(arr[i][j] + ans[i-1][j])
        ans.append(temp)    
t=[]
for i in ans:
    t.append(MAH(i,len(i)))
print(max(t))    

m=[[3,1], [2,2] ,[5,3], [3,4], [2,5] ,[4,6], [3,7]]
print(m[3][1])