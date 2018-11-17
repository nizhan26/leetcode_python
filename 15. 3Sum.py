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
        
        #Solution 1:
        #time consuming
        #T: O(n^2)
        #S: O(n)
        
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            #ignore repeated numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i] * -1
            s,e = i+1, n-1
            while s < e:
                if nums[s] + nums[e] == target:
                    ans.append([nums[i], nums[s], nums[e]])
                    s += 1
                    #ignore repeated numbers
                    while s<e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return ans
          
        
        #Solution 2:
        #get the number distribution first, faster,
        #but solution 1 is more suitable for normal cases
        cnt = {}
        for n in nums:
            cnt[n] = n in cnt and cnt[n] + 1 or 1
        pos, neg = [], []
        for n in cnt:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        ret = []
        if 0 in cnt and cnt[0] > 2:
            ret.append([0,0,0])
            
        pos.sort()
        neg.sort()
        for i in pos:
            for j in neg:
                t = 0-i-j
                if t in cnt:
                    if t == i or t == j:
                        if cnt[t] > 1:
                            ret.append([i,j,t])
                    elif i > t >=0 or 0 > t > j:
                        ret.append([i, j, t])
        return ret
    
    

        
