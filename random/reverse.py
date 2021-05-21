l = [1,23,45,63,24,64,66,86,46,278]
start = 0
end = len(l)-1
while(start<end):
 l[start],l[end] = l[end],l[start]
 start = start + 1
 end = end-1
print(l)
