#You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

#Return the shuffled string.

 

#Example 1:


#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
----------------------------------------------------------------------------------
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = ""
        for i in range (0 , len(indices)):
           new_string = new_string + s[indices.index(i)]
        return new_string 
            


            