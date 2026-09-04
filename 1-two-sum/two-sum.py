class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(len(nums)-1):
        #     f = target -  nums[i]
        #     for j in range(i+1,len(nums)):
        #         if f == nums[j]:
        #             result.append(i)
        #             result.append(j)

        # return result

        dict={}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in dict:
                return [dict[complement],i]

            dict[num]=i

        return []







        