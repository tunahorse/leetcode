Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    median = 0.0
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        
        # Adjusting the binary search.
        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        else:
            # We found the right partition.
            max_of_left = 0
            if i == 0: 
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            
            # Odd total length.
            if (m + n) % 2 == 1:
                return max_of_left * 1.0

            # Even total length.
            min_of_right = 0
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            
            return (max_of_left + min_of_right) / 2.0

    # Return 0.0 if no solution exists.
    return 0.0

# Testing the function with given examples
test_cases = [
    ([1, 3], [2]),
    ([1, 2], [3, 4])
]

results = [findMedianSortedArrays(nums1, nums2) for nums1, nums2 in test_cases]
results
