'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #Solution 1: Hash Table
        #to represent one key to many, use defaultdict(list), which is faster than the built-in function d.setdefault()
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        
        for a in range(len(nums) - 1):
            for b in range(a+1, len(nums)):
                is_duplicated = False
                for i,j in lookup[nums[a] + nums[b]]:
                    if nums[i] == nums[a]:
                        is_duplicated =True
                        break
                if not is_duplicated:
                    lookup[nums[a] + nums[b]].append((i,j))
        
        for c in range(2, len(nums) - 1):
            for d in range(c+1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for a,b in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            #different positions but could be the same result
                            if quad not in result:
                                result.append(quad)
        return result
        
        
        #Solution 2: recursion, but faster
        self.result = []
        
        def findNSum(l,r,N,target,result):
            #control the randomly chosen first two elements
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                #early termination
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        self.results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or nums[i] != nums[i-1]:
                        findNSum(i+1, r, N-1, target-nums[i], result+nums[i])
        nums.sort()
        findNSum(0, len(nums)-1, 4, target, [])
        return self.results
                            
        
