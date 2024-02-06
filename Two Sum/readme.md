# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:

Input: `nums = [2,7,11,15]`, `target = 9`  
Output: `[0,1]`  
Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2:

Input: `nums = [3,2,4]`, `target = 6`  
Output: `[1,2]`

### Example 3:

Input: `nums = [3,3]`, `target = 6`  
Output: `[0,1]`

### Constraints:

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Approach

To solve this problem efficiently, we can use a hash map (dictionary in Python) to store the indices of the numbers we have seen so far. This allows us to look up the complement of each number in constant time.

The steps are as follows:

1. Initialize an empty dictionary to store the indices of numbers.
2. Iterate through the array of numbers.
3. For each number, calculate the complement needed to reach the target.
4. If the complement exists in the dictionary, return the indices of the current number and its complement.
5. Otherwise, store the index of the current number in the dictionary.
6. If no solution is found after iterating through the entire array, return an empty list.

## How to Use

To use the solution provided in this repository:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the solution code.
4. Run the Python script containing the solution code.
5. Provide input array `nums` and target integer `target`.
6. The script will output the indices of the two numbers that add up to the target.

## Example

```python
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]

nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)  # Output: [1, 2]

nums = [3, 3]
target = 6
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
