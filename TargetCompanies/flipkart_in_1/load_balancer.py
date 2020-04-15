"""
Design a load balancer which implements following methods:
add(n) where n is id of instance
remove(n) where n is id of instance
getRandom() which returns a random instance.

All these operation should be of order O(1).
"""

####Answer

"""
Consider a data structure composed of a hashtable H and an array A.
The hashtable keys are the elements in the data structure,
and the values are their positions in the array.

insert(value): append the value to array and let i be its index in A. Set H[value]=i.
remove(value): We are going to replace the cell that contains value in A with the last element in A. let d be the last element in the array A at index m. let i be H[value], the index in the array of the value to be removed. Set A[i]=d, H[d]=i, decrease the size of the array by one, and remove value from H.
contains(value): return H.contains(value)
getRandomElement(): let r=random(current size of A). return A[r].
since the array needs to auto-increase in size, it's going to be amortize O(1) to add an element, but I guess that's OK.

Side note:
O(1) lookup implies a hashed data structure.

By comparison:

O(1) insert/delete with O(N) lookup implies a linked list.
O(1) insert, O(N) delete, and O(N) lookup implies an array-backed list
O(logN) insert/delete/lookup implies a tree or heap.

"""