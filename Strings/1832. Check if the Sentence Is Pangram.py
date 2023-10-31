#A pangram is a sentence where every letter of the English alphabet appears at least once.

#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

#Example 1:

#Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
#Output: true
#Explanation: sentence contains at least one of every letter of the English alphabet.
--------------------------------------------------------------------------------------------------
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char = set(sentence)
        sorted_set = ''.join(sorted(char))
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in sorted_set:
            for j in alphabets:
                if len(sorted_set) == len(alphabets):
                    return True
                else:
                    return False
        
        
                
                   