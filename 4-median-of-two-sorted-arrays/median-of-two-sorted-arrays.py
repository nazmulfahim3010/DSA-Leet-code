class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listy = sorted(nums1+nums2)
        
        if len(listy)%2==0:
            mid=len(listy)//2
            return (listy[mid]+listy[mid-1])/2.00
        else:
            mid= len(listy)//2
            return listy[mid]+0.00000


        


        
        