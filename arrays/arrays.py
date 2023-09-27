# return true if it the array contains duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            
            else:
                hashset.add(n)

        return False
    


    