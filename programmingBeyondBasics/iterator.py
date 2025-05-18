"""

Iterators in Python is a design pattern
- it abstracts away repetive logic, eg range(10), zip(10) etc
- if you run 
    - x = range(10)
    - type(x)
    - you will see that x is not a list rather its its own class
        - this means that range() is not stored in memory
        - makes sense cuz why do we want to store it in memory anyways?


objective of this excercise is to build that interface from scratch


"""
class MyRange:
    """
    Custom implementation of Python's range function.
    
    This class mimics the functionality of the built-in range() function,
    providing a way to iterate through a sequence of numbers from 0 to end-1.
    """
    def __init__(self, end):
        self.n = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.end:
            raise StopIteration
        current = self.n
        self.n += 1
        return current

    def __reversed__(self):
        class Reversed:
            """
            Nested class that provides reversed iteration functionality.
            
            This class allows MyRange to be used with the reversed() built-in function.
            """
            def __init__(self, start, end):
                self.n = end - 1
                self.start = start

            def __iter__(self):
                return self

            def __next__(self):
                if self.n < self.start:
                    raise StopIteration
                current = self.n
                self.n -= 1
                return current

        return Reversed(0, self.end)



y = MyRange(10)


for x in y:
    print(x)

for x in reversed(y):
    print(x)
