class Solution:
    def isValid(self, s: str) -> bool:
      blacketDict = {
        "[": "]", 
        "{": "}", 
        "(": ")"
      }
      open_list = []

      isValid = True

      for element in s:
        # if it is open one
        if element == "[" or  element == "{" or  element == "(":
            open_list.append(element)
        else:
            if len(open_list) == 0:
                isValid = False
                break
            else:
                # if it is close one
                # get first of open_list and remove first open_list if blacket is closed
                if blacketDict[open_list[-1]] == element:
                    open_list.pop(-1)
                else:
                  isValid = False
                  break

      return len(open_list) == 0 and isValid