class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        empty_list = []
        for i in range(n):
            empty_list = empty_list + [nums[i]]
            empty_list = empty_list + [nums[i+n]]
        return empty_list