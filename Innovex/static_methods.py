# static methods - belongs to a class rather than instance of the class
"""
- they don't require access to instance or class itself
- can be called on both the class itself and the instance of the class
"""


class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


print(Math.add(34, 23))
ops = Math()
print(ops.add(23, 434))
