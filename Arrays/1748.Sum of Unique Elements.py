#You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

#Return the sum of all the unique elements of nums.

 

#Example 1:

#Input: nums = [1,2,3,2]
#Output: 4
#Explanation: The unique elements are [1,3], and the sum is 4.
----------------------------------------------------------------------
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        new_dict = collections.defaultdict(int)
        sum_numbers = 0 
        for num in nums:
            new_dict[num]+=1
        for key,value in new_dict.items():
            if value == 1:
                sum_numbers+= key 
        return sum_numbers
            
        