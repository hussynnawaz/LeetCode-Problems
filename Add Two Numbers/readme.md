# Add Two Numbers

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1:

Input: `l1 = [2,4,3]`, `l2 = [5,6,4]`  
Output: `[7,0,8]`  
Explanation: `342 + 465 = 807`.

### Example 2:

Input: `l1 = [0]`, `l2 = [0]`  
Output: `[0]`

### Example 3:

Input: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`  
Output: `[8,9,9,9,0,0,0,1]`

### Constraints:

- The number of nodes in each linked list is in the range [1, 100].
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Approach

To add two numbers represented by linked lists efficiently, we iterate through both lists simultaneously, adding corresponding digits along with any carry. We initialize a dummy head node to facilitate the creation of the result linked list. The steps are as follows:

1. Initialize variables to store the result and carry.
2. Traverse both linked lists simultaneously.
3. Calculate the sum of corresponding digits and carry.
4. Create a new node with the result digit and update the carry.
5. Move to the next nodes in both lists.
6. Handle any remaining carry after the traversal.
7. Return the result linked list.

## How to Use

To use the solution provided in this repository:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the solution code.
4. Run the Python script containing the solution code.
5. Provide input linked lists `l1` and `l2`.
6. The script will output the sum of the two numbers as a linked list.

## Example

```python
# Example usage:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Output: [7,0,8]
while result:
    print(result.val, end=" ")
    result = result.next
