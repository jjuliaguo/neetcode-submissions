class MinStack:

    def __init__(self):

        #need self. because otherwise it's local variable and initialization doesn't work beyond method
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None: #if it's -> None, don't return anything
        self.minStack.pop()

        #in answer, pops both because if that was the min number then obv it's no longer there -> make sure to update minStack too

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int: # right now getMin is O(n) since checking every element
        min = float('inf')
        for element in self.minStack: 
            if element < min:
                min = element
        return min

    #def push(self, val: int) -> None:
    #self.stack.append(val)
    #when minStack isn't empty, the most current min is last element, otherwise it's just current val
    #val = min(val, self.minStack[-1] if self.minStack else val)
    #$self.minStack.append(val)
        
