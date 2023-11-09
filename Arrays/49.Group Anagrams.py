#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

#Example 1:

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]] 
-------------------------------------------------------------------
Class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            t = ''.join(sorted(word))
            
            if t not in dictionary:
                #creating a new key value pair
                dictionary[t]=[word]
            else:
                dictionary[t].append(word)
        return dictionary.values()       