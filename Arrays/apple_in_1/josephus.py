class Josephus:
    def __init__(self):
        print("Init")
        #self.num = n
        #self.k = k
        #print (getJosephus(n,k));

    def getJosephus(self, n, k):
        #print("{} {}".format(n,k))
        if(n==1):
            return 0;
        else:
            return (self.getJosephus(n-1,k)+k)%n;

n=int(input())
k=int(input())
p = Josephus()
print(p.getJosephus(n,k));