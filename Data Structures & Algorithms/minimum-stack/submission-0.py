class MinStack:

    def __init__(self):

        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None: #if it's -> None, don't return anything
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        min = float('inf')
        for element in self.minStack:
            if element < min:
                min = element
        return min
        
