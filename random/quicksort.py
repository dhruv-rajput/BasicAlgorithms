def partition(arr,low,high): 
    i = (low-1)    
    pivot = arr[high]   
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr,low,high) 
        quickSort(arr, low, p-1) 
        quickSort(arr, p+1, high) 
  
arr = [5,7,9,0,4,6,2,7,2,8,10,3,4,5,6] 
quickSort(arr,0,len(arr)-1) 
print(*arr) 
  