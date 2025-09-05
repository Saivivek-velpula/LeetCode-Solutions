class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d1={}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in d1:
                return [i,d1[dif]]
            else:
                d1[nums[i]]=i