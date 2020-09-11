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
        for i in range(len(A)):
            median.add_number(A[i]) # 2 7
            print("{} {}".format(A[i], median.get_median()))
            if(median.get_median()==A[i] and i!=0):
                print(median.get_median(), A[i])
                return 1
        median2 = RunningMedian()
        for i in range(len(A))[::-1]:
            median2.add_number(A[i])
            print("{} {}".format(A[i], median2.get_median()))
            if(median2.get_median()==A[i] and i!=len(A)-1):
                print(median2.get_median(), A[i])
                return 1
        return 0


solution = Solution()
A = [2,7,3,1]
print(solution.solve(A))