#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
 

#Example 1:

#Input: s = "()"
#Output: true
------------------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"(":")","{":"}","[":"]"}
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack)!=0 and parenthesis.get(stack[-1]) == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            
        return len(stack)==0

            