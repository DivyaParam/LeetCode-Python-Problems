class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0 
        for operation in range(len(operations)):
            
            if operations[operation] == "++X" or operations[operation] == "X++":
                count = count+1
            else:
                count = count-1
