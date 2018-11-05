#Description:
#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#You may assume nums1 and nums2 cannot be both empty.

#T: O(log(m+n)) #which indicate we must divide each sublist by half
#S: O(m+n) #the exponent of log(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #two pointers in the middle of the sorted arrays at start, moves half of its order according to its order sum comparison with the target
        #badbad, the median k could show up in the same array
        #the solution is a recursion algorithm
 
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2
        
        if (m + n) % 2 == 0:
            return (self.findk(nums1, nums2, k) + self.findk(nums1, nums2, k-1))/2
        else:
            return (self.findk(nums1, nums2, k))
            
    #find the kth number of the two sorted lists    
    def findk(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])

        len1, len2 = len(nums1), len(nums2)
        
        #if the first median is larger than the second median
        if nums1[len1 // 2] > nums2[len2 // 2]:
            if k > len1 // 2 + len2 // 2:
            #the number we want to find can not lie in 0-> len2//2
                return self.findk(nums1, nums2[len2 // 2 + 1:], k - len2//2 - 1 )
            else:
                return self.findk(nums1[:len1 // 2], nums2, k)
        else:
            if k > len1 // 2 + len2 // 2:
                return self.findk(nums1[len1 // 2 + 1:], nums2, k - len1//2 - 1 )
            else:
                return self.findk(nums1, nums2[:len2 // 2], k)
