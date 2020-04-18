A = [1, 2, 3, 4, -10]
def find_largest_contiguous_array(A):
    max_so_far = 0;
    max_ending_her = 0;
    for i in A:
        max_ending_her = max_ending_her + i;
        if(max_ending_her<0):
            max_ending_her = 0
        if(max_so_far < max_ending_her):
            max_so_far = max_ending_her
    return max_so_far;

print(find_largest_contiguous_array(A))
        