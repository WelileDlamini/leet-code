class Solution:
     def defangIPaddr(self, address: str) -> str:
          
        final_result = address.replace(".", "[.]")

        return final_result
     
