class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
          ")": "(",
          "]": "[",
          "}": "{"
        }
        retVal = False
        if len(s) % 2 == 0:
               stack = []
               for ch in s:
                   if len(stack) == 0:
                       stack.append(ch)
                   elif dict.get(ch) != None and dict[ch] == stack[-1]:
                       stack.pop()
                   else:
                       stack.append(ch)
               
               if len(stack) == 0:
                   retVal = True
        
        return retVal