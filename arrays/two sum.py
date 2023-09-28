## two sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        prevMap = {} # val : index # dictioinary

        for i , n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i 

        return 



# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1] # check what this does
        elif s < target:
            l += 1
        else:
            r -= 1
