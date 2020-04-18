A = [1,2,3,4,5]
B = 10
def find_max_size_subarray(A, B, mid):
    #prefix = []
    #prefix.append(A[0])
    s = 0
    for i in range(0, mid):
        s+=A[i]
        #prefix.append(A[i]+ prefix[i-1])
    if(s>B):
        return False;
    for i in range(mid, len(A)):
        s+=A[i]-A[i-mid]
        if(s>B):
            return False
    #print(mid, end=' ')
    return True
    #print(prefix, end=' ')

l = 1; 
r = len(A)
while l<=r:
    mid = (l+r) >> 1
    if(find_max_size_subarray(A, B, mid)):
        l = mid+1;
    else:
        r = mid-1;
print(l-1)



#find_max_size_subarray(A)