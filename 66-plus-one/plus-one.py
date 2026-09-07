class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num =0
        result =[]

        for i in digits:
            num = num*10 + i

        num+=1

        num = str(num)

        for n in num:
            result.append(int(n))
        
        return result