#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

#Example 1:

#Input: s = "leetcodeisacommunityforcoders"
#Output: "ltcdscmmntyfrcdrs"
--------------------------------------------------------------
class Solution:
    def removeVowels(self, s: str) -> str:
        
        array = []
        for i in range(0, len(s)):
            if s[i] not in 'aeiou':
                print(s[i])
                array.append(s[i])
        return''.join(array)