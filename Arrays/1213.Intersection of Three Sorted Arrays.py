#Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

#Example 1:

#Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
#Output: [1,5]
#Explanation: Only 1 and 5 appeared in the three arrays.
-------------------------------------------------------------------class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        new_dictionary = collections.defaultdict(int)
        result = []
        for num1 in arr1:
            new_dictionary[num1]+=1
        for num2 in arr2:
            new_dictionary[num2]+=1
        for num3 in arr3:
            new_dictionary[num3]+=1
        for key,value in new_dictionary.items():
            if (value ==3):
                result.append(key)

        return result
        
        
        
        
        
     
        