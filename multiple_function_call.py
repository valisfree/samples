class testClass(int):
    def __call__(self, x):
        return testClass(self + x)

def add(i):
    return testClass(i)
print(add(5)(6))

