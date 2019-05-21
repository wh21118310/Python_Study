class test:
    def __init__(self,a):
        self.data = a[:]
    def __add__(self, obj):
        x = len(self.data)
        y = len(obj.data);
        max = x if x>y else y
        n1 = []
        for n in range(max):
            n1.append(self.data[n]+obj.data[n])
        return test(n1[:])
x = test([1,2,3])
y = test([1,2,3,4,5])
z = x+y;
print(z.data);