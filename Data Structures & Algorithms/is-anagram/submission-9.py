class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.get_map_of_str(s)
        t_map = self.get_map_of_str(t)
        if s_map == t_map:
            return True
        else:
            return False    

    def get_map_of_str(self, s: str):
        map_of_str = {}

        for character in s:
            map_of_str[character] = 0
        
        for character in s:
            if character in map_of_str.keys():
              map_of_str[character] =   map_of_str[character] + 1
        
        return map_of_str
                