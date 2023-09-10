# best time to buy and sell stock
class Solution:
    def maxProfit(self,price: List[int]) -> int:
        l,r = 0,1 #left buy, right sell
        maxP = 0

        while r < len(price):
            # profitable
            if price[l] < price[r]:
                profit = price[r] - price[l]
                maxP = max(maxP, profit)

            else:
                l = r

            r += 1

# longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0


        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1) # check

        return res
    
# longest repeating character replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-1+1) - max(count.values()) > k:
                count[s(l)] -= 1
                l += 1

            res = max(res, r-1+1)

        return res
    

# mininum window substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == " ": return " "

        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]

        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update our result
            if (r-1+1) < resLen:
                res = [l, r]
                resLen = (r-1+1)

            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

        l, r = res

        return s[l:r+1] if resLen != float("infinity") else " "
    

    # stack
    





                       





    


