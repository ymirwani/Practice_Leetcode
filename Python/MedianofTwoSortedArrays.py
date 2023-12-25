# created by ymirwani

'''
4. Median of Two Sorted Arrays [Hard]
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''

import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # ls1, ls2 = len(nums1), len(nums2)
        # if ls1 < ls2:
        #     return self.findMedianSortedArrays(nums2, nums1)
        # l, r = 0, ls2 * 2
        # while l <= r:
        #     mid2 = (l + r) >> 1
        #     mid1 = ls1 + ls2 - mid2
        #     L1 = -sys.maxint - 1 if mid1 == 0 else nums1[(mid1 - 1) >> 1]
        #     L2 = -sys.maxint - 1 if mid2 == 0 else nums2[(mid2 - 1) >> 1]
        #     R1 = sys.maxint if mid1 == 2 * ls1 else nums1[mid1 >> 1]
        #     R2 = sys.maxint if mid2 == 2 * ls2 else nums2[mid2 >> 1]
        #     if L1 > R2:
        #         l = mid2 + 1
        #     elif L2 > R1:
        #         r = mid2 - 1
        #     else:
        #         return (max(L1, L2) + min(R1, R2)) / 2.0
        s=nums1+nums2
        s.sort()
        l=len(s)
        if l%2!=0:
            return s[l//2]
        else:
            return (s[l//2]+s[l//2-1])/2.0000
        
if __name__ == '__main__':
    # call the class and log
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([1, 2], [3]))
    # runtime 1st code is 60ms and 2nd code is 15ms