#You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

#The ith item is said to match the rule if one of the following is true:

#ruleKey == "type" and ruleValue == typei.
#ruleKey == "color" and ruleValue == colori.
#ruleKey == "name" and ruleValue == namei.
#Return the number of items that match the given rule.

 

#Example 1:

#Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
#Output: 1
#Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0 
        dictionary = {"type":0,"color":1,"name":2}
        for i in items:
            if i[dictionary[ruleKey]]==ruleValue:
                count = count +1
        return count 
            