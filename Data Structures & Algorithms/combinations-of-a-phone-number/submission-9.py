class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        phone = {"2" : "abc",
                 "3" : "def",
                 "4" : "ghi",
                 "5" : "jkl",
                 "6" : "mno",
                 "7" : "pqrs",
                 "8" : "tuv",
                 "9" : "wxyz"}
                
        res = []
        def backtrack(i, currStr):
            if i >= len(digits):
                res.append(currStr)
                return
            
            for c in phone[digits[i]]:
                backtrack(i + 1, currStr + c)
        
        backtrack(0, "")
        return res