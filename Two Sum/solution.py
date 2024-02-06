from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # If the complement is in the dictionary, return the indices
            if complement in num_indices:
                return [num_indices[complement], i]
            
            # Otherwise, store the index of the current number
            num_indices[num] = i
        
        # If no solution is found, return an empty list
        return []
