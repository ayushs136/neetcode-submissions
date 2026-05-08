class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partitions = []
        
        def isPalindrome(s):
            
            return s == s[::-1]

        def getPartitions(s, res, partitions):
            if len(s) == 0:
                res.append(partitions.copy())
                return
            for i in range(len(s)):
                
                part = s[0:i+1]

                if isPalindrome(part):
                    partitions.append(part)
                    getPartitions(s[i+1:], res, partitions)
                    partitions.pop()


                

    
        getPartitions(s, res, partitions)
        return res