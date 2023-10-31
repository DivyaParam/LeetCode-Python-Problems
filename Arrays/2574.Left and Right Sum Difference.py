#Problem Statement
#Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

#answer.length == nums.length.
#answer[i] = |leftSum[i] - rightSum[i]|.
#Where:

#leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
#rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
#Return the array answer.

 

#Example 1:

#Input: nums = [10,4,8,3]
#Output: [15,1,11,22]
#Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
#The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
----------------------------------------------------------------------------------------------------------
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]*len(nums)
        right_sum = [0]*len(nums)
        difference = [0]*len(nums)
        #left_sum array calculation 
        for i in range(1,len(nums)):
            left_sum[i]= left_sum[i-1]+nums[i-1]
        #right_sum array calculation 
        for j in range(len(nums)-2, -1,-1):
            right_sum[j] = nums[j+1]+right_sum[j+1]
        #calculating the difference array
        for k in range(0,len(nums)):
            difference[k] = abs(left_sum[k] - right_sum[k])
            
        return difference


