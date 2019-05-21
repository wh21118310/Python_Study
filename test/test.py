class test:
    def __init__(self,a):
        self.data = a[:]
    def __add__(self, obj):
        x = len(self.data)
        y = len(obj.data)
        max = x if x>y else y
        n1 = []
        for n in range(max):
              n1.append(self.data[n]+obj.data[n])
        return test(n1[:])
try:
      x = test([1,2,3,4])
      y = test([10,20,30])
      z = x+y
      print(z.data)
except (IndentationError, ZeroDivisionError, TabError,IndentationError) as In:
        print("异常类型" + In.__class__.__name__)
        print("异常信息： " + In)


