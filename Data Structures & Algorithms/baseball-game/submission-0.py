class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        #always be at least 2 before +, C, D

        result = []

        for index in range(len(operations)):
            if operations[index] == "+":
                result.append(result[-2] + result[-1])
                #result.append(operations[index-2] + operations[index-1])
            elif operations[index] == "D":
                result.append(result[-1] * 2)
                #result.append(operations[index-1] * 2)
            elif operations[index] == "C":
                #pop automatically removes last element -> can also do pop(-1)
                result.pop()
                #result.pop(index-1)
            else:
                result.append(int(operations[index]))

        total = sum(result)
        return total  