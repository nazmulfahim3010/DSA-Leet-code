class Solution:
    def reverse(self, x: int) -> int:

        # time 0(n)  space O(n)


        # num = str(x)[::-1]
        # result =0
        # if "-" in num:
        #     num = list(num)
        #     num.remove("-")
        #     num = "".join(num)
        #     result = int(num) *-1
        # else:
        #     result = int(num)

        # if result < -2**31 or result > 2**31 - 1:
        #     return 0
        
    
        # return result


        # time O(n) space O(1)

        if x > 0:
            check = 1
        elif x < 0:
            check = -1
        else:
            check = 0   

        num = abs(x)
        result=0

        while(num>0):
            digit= num%10
            
            result = result*10 + digit

            num//=10

        if result< -2**31 or result > 2**31-1:
            return 0
        
        return result*check

