# Grind 75
Approaches and solutions to Grind 75 leetcode questions

## Week 1


### [1. Two Sum](https://leetcode.com/problems/two-sum/)

**Approach**

- Only one pass through the entire array.
- Keep checking if `target - current number` exists in a hashmap.
- If it does, we have found the pair.
- If not, store current number and its index in the hashmap to be discovered later.

**Time complexity**

O(N) since we make only one pass through the entire array.

**Space complexity**

O(N) since we store all numbers in a hashmap in the worst case.

### [2. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Approach**

- One single pass through the array
- Keep the characters in a stack if it's an opening bracket
- If it's a closing bracket, check if a corresponding opening bracket exists in the stack top.
    - if it does, pop from the stack
    - else if the stack is empty or a matching opening bracket doesn't exist, this is invalid
- after going through the entire sequence, the stack should be empty. Otherwise, there are some unmatched brackets which make the sequence invalid.

**Time complexity**

O(N) since we check each character only once.

**Space complexity**

O(N) for the extra stack.


### [3. Merge two sorted lists](https://leetcode.com/problems/merge-two-sorted-lists/)

**Approach**

- Handle base cases: if one of the lists are empty, return the other.
- compare the value at the head of the lists.
- Recursively update the next pointer of the lists depending on which one has the smaller value.

**Time complexity**

O(N) where N is the total length of both the lists. Since we encounter each node only once, it's linear.

**Space complexity**

O(N) due to recursion stack.

### [4. Buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Approach**

- One single pass through the array.
- Keep track of the minimum seen so far and the maximum profit obtained so far.
- If you see a price bigger than the minimum price so far, update max profit.
- If you see a price smaller than the minimum price, update minimum price so far.


**Time Complexity**

O(N) since we encounter each price only once.

**Space Complexity**

O(1) since we don't use any extra space.