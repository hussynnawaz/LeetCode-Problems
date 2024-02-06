# Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

### Example 1:

Input: `nums1 = [1,3]`, `nums2 = [2]`  
Output: `2.00000`  
Explanation: Merged array = `[1,2,3]` and median is `2`.

### Example 2:

Input: `nums1 = [1,2]`, `nums2 = [3,4]`  
Output: `2.50000`  
Explanation: Merged array = `[1,2,3,4]` and median is `(2 + 3) / 2 = 2.5`.

### Constraints:

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-106 <= nums1[i], nums2[i] <= 106`

## Approach

The problem can be solved efficiently using a binary search algorithm. The basic idea is to partition both arrays such that the elements on the left side are less than or equal to the elements on the right side. By ensuring this condition, we can find the median of the merged array.

## How to Use

To use the solution provided in this repository:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the solution code.
4. Run the Python script containing the solution code.
5. Provide input arrays `nums1` and `nums2`.
6. The script will output the median of the two sorted arrays.

## Example

```python
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.5
