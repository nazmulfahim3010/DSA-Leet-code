class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        is_pal= True
        length = len(num)
        if len(num)%2==0:
            l,r=(length//2)-1,(length//2)
            while (l>=0 and r<len(num) and is_pal==True):
                if num[l]==num[r]:
                    l-=1
                    r+=1
                else:
                    is_pal = False
        else:
            l,r=length//2,length//2
            while (l>=0 and r<len(num) and is_pal==True):
                if num[l]==num[r]:
                    l-=1
                    r+=1
                else:
                    is_pal = False

            
        if is_pal:
            return True
        else:
            return False



        