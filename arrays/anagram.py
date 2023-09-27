class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        if len(s) != len(t):
            return False
        
        countS, CountT = {}, {}

        for i in range(len(s)): # iterating through strings since they are both equal
            countS[s[i]] = 1 + countS.get(s[i], 0) # count the occurance of each character in s
            CountT[t[i]] = 1 + CountT.get(t[i], 0)

        for c in countS: # iterating through the hashmaps
            if CountT[c] != countS.get(c, 0):
                return False
            
        return True
    

# you can also use counter which is a hashmap in python
# since counter is a data structer in python which actually counts things

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:

        return Counter(s) == Counter(t)
    
# you can also sort them
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:

        return sorted(s) == sorted(t) # this will return True or False
    
    
            
