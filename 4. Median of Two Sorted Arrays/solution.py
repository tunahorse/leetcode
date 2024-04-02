# #psudo
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Main problem, find the median of two sorted arrays
# Find median, while keeping track of the number of elements in each array

from typing import List

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print('Starting Data')
        print(nums1, nums2)
        
        
        # Make's sure the first array is the smallest, for faster search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            print('Swapped the arrays')
            print(nums1, nums2)

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        print('Initial Values')
        print(imin, imax, half_len)

        # search begins in the smaller array.
        while imin <= imax:
            # Find a partition in nums1.
            i = (imin + imax) // 2
            # Makes the search space smaller.
            j = half_len - i
            
            # If nums1[i] is too small, increase i.
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            # If nums1[i-1] is too big, decrease i.
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # Correct partition found.
            else:
                # Find the largest value on the left side.
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                # If the total length is odd, return the max of left side directly.
                if (m + n) % 2 == 1:
                    return max_of_left

                # Find the smallest value on the right side.
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                # If the total length is even, return the average of max_of_left and min_of_right.
                return (max_of_left + min_of_right) / 2
solution = Solution()


print(solution.findMedianSortedArrays([1,3], [2]))  # Expected: 2.0

# Class Definition & Method Signature: A class named Solution is defined with a method findMedianSortedArrays.
# This method accepts two sorted arrays nums1 and nums2 and returns the median as a float.

# Ensure nums1 is the Smaller Array: To optimize the search space for the binary search, the method ensures that nums1 is the smaller array. 
# If it's not, nums1 and nums2 are swapped.
# Initialize Variables:
# m and n store the lengths of nums1 and nums2, respectively.
# imin and imax are the starting and ending indices for the binary search in nums1.
# half_len calculates the halfway point across both arrays, aiding in determining the correct partition.
# Binary Search Loop: The loop runs until the correct partition is found. It modifies imin and imax to narrow down the search space in nums1.
# Find Partitions i and j: i is the current partition index in nums1 found by binary search. j is the corresponding partition index in nums2, calculated so that the left side of the partitions contains half of the elements (or one more if the total number of elements is odd).
# Adjusting i: If nums1[i] is too small, indicating not enough elements on the left side of nums1, imin is adjusted. If nums1[i-1] is too big, indicating too many elements on the left side, imax is adjusted.
# Correct Partition Found: When the correct partition is found (none of the above conditions are true), it calculates the largest element on the left side (max_of_left) and the smallest element on the right side (min_of_right).
# Calculate Median: The median is calculated differently based on whether the total number of elements is odd (return max_of_left) or even (return the average of max_of_left and min_of_right).
# This approach ensures that the time complexity is O(log(min(m, n))) by performing a binary search on the smaller of the two arrays.

