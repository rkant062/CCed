from heapq import heappush, heappop

class RunningMedian:
    def __init__(self):
        self.lowers, self.highers = [], []

    def add_number(self, number):
        if not self.highers or number > self.highers[0]:
            heappush(self.highers, number)
        else:
            heappush(self.lowers, -number)  # for lowers we need a max heap
        self.rebalance()

    def rebalance(self):
        if len(self.lowers) - len(self.highers) > 1:
            heappush(self.highers, -heappop(self.lowers))
        elif len(self.highers) - len(self.lowers) > 1:
            heappush(self.lowers, -heappop(self.highers))

    def get_median(self):
        if len(self.lowers) == len(self.highers):
            return (-self.lowers[0] + self.highers[0])/2
        elif len(self.lowers) > len(self.highers):
            return -self.lowers[0]
        else:
            return self.highers[0]
            
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        median = RunningMedian()
        for i in range(len(A)-1):
            median.add_number(A[i+1])
            if(median.get_median()==A[i+1]):
                print(median.get_median(), A[i+1])
                return 1
        for i in range(A, -1, -1):
            median.add_number(i)
            if(median.get_median()==i):
                print(median.get_median(), i)
                return 1
        return 0


solution = Solution()
A = [1,2,3,4,5,6]
print(solution.solve(A))
        