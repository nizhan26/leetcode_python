'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #Solution 1: recursion
        #T: O()
        #S: O()
        
        nums.sort()
        sol = []
        
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                l = [nums[i], nums[l], nums[r]]
                
                if sum(l) == 0:
                    sol.append(l)
                    r -= 1
                    l += 1
                
                    #ignore repeated numbers
                    while nums[l] == nums[l-1] and l<r:
                        l -= 1
                    while nums[r] == nums[r+1] and l<r:
                        r -= 1
                elif sum(l) > 0:
                    r -= 1
                else:
                    l += 1
                    
            i += 1
                
            #ignore repeated numbers
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
                
        return sol
                    
