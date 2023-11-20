#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

------------------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        result = []
        for num in nums:
            if num not in dictionary:
                dictionary[num]=1
            else:
                dictionary[num]+=1

        for i in range(k):
            max_count = (max(dictionary, key=dictionary.get))
            result.append(max_count)
            del dictionary[max_count]
        return result