class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def generate(curr, open, close):

            if open == close == n:
                result.append(curr)
                return

            if open<n:
                generate(curr+'(', open+1, close)
            
            if close<open:
                generate(curr+')', open, close+1)

        generate("", 0, 0)
        return result