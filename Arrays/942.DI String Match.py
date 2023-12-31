#A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

#s[i] == 'I' if perm[i] < perm[i + 1], and
#s[i] == 'D' if perm[i] > perm[i + 1].
#Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

#Example 1:

#Input: s = "IDID"
#Output: [0,4,1,3,2]
---------------------------------------
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0 
        high = len(s)
        result = []
        for i in s:
            if i == 'I':
                result.append(low)
                low+=1
            elif i == 'D':
                result.append(high)
                high-=1
        return result + [low]

        