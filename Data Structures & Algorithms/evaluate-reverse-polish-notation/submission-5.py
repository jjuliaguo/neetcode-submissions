class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

    #Questions
    # Is there a chance that operator has no number before it?

        nums = []
        
        for element in tokens:
            if element == "+":
                sum = int(nums[-2]) + int(nums[-1])
                nums.pop()
                nums.pop()
                nums.append(sum)
            elif element == "-":
                sub = int(nums[-2]) - int(nums[-1])
                nums.pop()
                nums.pop()
                nums.append(sub)
            elif element == "*":
                product = int(nums[-2]) * int(nums[-1])
                nums.pop()
                nums.pop()
                nums.append(product)
            elif element == "/":
                quot = int(nums[-2]) / int(nums[-1])
                nums.pop()
                nums.pop()
                nums.append(quot)
            else: 
                nums.append(element)

        return int(nums[-1])
