#brute force
#T: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
                
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
#because there is only unique solution to this problem, so we build a dictionary to store the value as key in dict 
#, the order as value, so that we can solve this problem by one scanning
#T: O(n)
#S: O(n)
        keys = {}
        for i in range(len(nums)):
            if nums[i] not in keys:
                keys[nums[i]] = i
            if nums[i] - target in keys:
                return [keys[nums[i] - target], i]
 
      
