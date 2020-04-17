'''
Maximum Frequency stack
You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it. Operations are of two types:
1 x: push an integer x onto the stack and return -1
2 0: remove and return the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.
A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.

Input 1:
    A = A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Output 1:
    [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]

'''
from collections import deque, defaultdict
A = [
    [1, 5],
    [1, 7],
    [1, 5],
    [1, 7],
    [1, 4],
    [1, 5],
    [2, 0],
    [2, 0],
    [2, 0],
    [2, 0]]
stack = []
most_freq_num = 0


def get_max_feq_stack(A):
    stk = []
    temp = []
    map = defaultdict(lambda: 0)
    res = []
    for i in A:
        if i[0] == 1:
            x = i[1]
            if not stk:
                stk.append([x, 1])
                map[x] = 1

            else:
                map[x] += 1
                freq = map[x]
                while stk and stk[-1][1] > freq:
                    temp.append(stk.pop())

                stk.append([x, freq])

                while temp:
                    stk.append(temp.pop())

            res.append(-1)

        else:
            x = stk.pop()
            map[x[0]] -= 1
            res.append(x[0])

    return res


print(get_max_feq_stack(A))
