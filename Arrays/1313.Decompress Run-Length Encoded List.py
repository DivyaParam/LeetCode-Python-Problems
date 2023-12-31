#We are given a list nums of integers representing a list compressed with run-length encoding.

#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

#Return the decompressed list.
#Example 1:

#Input: nums = [1,1,2,3]
#Output: [1,3,3]
------------------------------------------------------------------------------------------------------
Class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range (0,len(nums),2):
            result = result + nums[i]*[nums[i+1]]
        return result