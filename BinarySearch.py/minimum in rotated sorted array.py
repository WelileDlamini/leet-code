

# fiding the minimum in a sorted array

class Solution:
    def findMin(self, num: List[int]) -> int:
        res = num[0]
        l,r = 0, len(num)-1



        while l <= r:
            if num[l] < num[r]:
                res = min(res, num[l])
                break

            m = (l + r) // 2
            res = min(res, num[m])

            if num[m] >= num[l]:
                l = m + 1

            else:
                r = m - 1

        return res
    


# search in rotated sorted array GOOGLE
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)- 1

        
        # [1]
        while l <= r:
            mid = (l+r)// 2

            if target == nums[mid]:
                return mid
            
            # left sorted potion

            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1

                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            else: #right sorted portion
                if target < nums[mid]:
                    r = mid - 1

                elif target > nums[r]:
                    r = mid - 1

                else:
                    l = mid + 1

        return -1
    
    










    


