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