'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Solution 1 - not optimal
        #T: O(n^2)
        
        nums.sort()
        i = 0
        closest = nums[0] + nums[1] + nums[2]
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                
                #update closest
                if abs(sums - target) < abs(closest - target):
                    closest = sums
                    
                #adjust pointers based on target
                #ignore repeated numbers
                if sums < target:
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif sums > target:
                    k -= 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                else:
                    return target
                    
            i += 1
            while nums[i] == nums[i-1] and j < k:
                i += 1
        return closest
        
        
        #Solution 2
        #save scanning of choosing i
        #T: O(n^2)
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) -1
            if nums[i] + nums[k] + nums[k-1] < target:
                res.append(nums[i] + nums[k] + nums[k-1])
            elif nums[i] +  nums[j] + nums[j+1] > target:
                res.append(nums[i] + nums[j] + nums[j+1])
            else:
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    res.append(s)
                    if s < target:
                        j += 1
                    elif s > target:
                        k -= 1
                    else:
                        return target
        res.sort(key = lambda x: abs(x-target))
        return res[0]
        
