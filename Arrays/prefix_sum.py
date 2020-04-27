def find_total_length(A):
    pref_sum = [0]*(len(A)+1)
    #pref_sum
    n = len(A)
    pref_sum[0] = A[0]
    for i in range(1,n):
        print(i)
        pref_sum[i] = pref_sum[i-1]+A[i]
    return pref_sum[:n]

A = [1,2,3,4,5]
print(find_total_length(A))