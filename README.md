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

### [5. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Approach**

- make the entire string lower-case
- use two-pointers.
    - the left pointer ignores non-alphanumeric characters from the left by skipping forward.
    - the right pointer ignores non-alphanumeric characters from the right by skipping backward.
- when both pointers point to an alphanumeric character, compare them.
- if at any point, the pointers point to different characters, it can't be a palindrome
- it's a valid palindrome if both pointers cross each other without failure.

**Time Complexity**

O(N) because of a single pass through the string.

**Space Complexity**

O(1) since we don't use any extra space.


### [6. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Approach**

- Handle base cases
    - Empty tree
    - Only one node in the tree
- Invert tree for the left and right subtrees recursively
- Handle the inverted left and right sub-trees at the root
- Return the root

**Time Complexity**

O(N) since we do constant work at each node.

**Space Complexity**

O(N) for recursion stack if the tree is like a linked-list (skewed, only left/right child at each node)


### [7. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

**Approach**

- Anagram: Frequency of characters in both the strings should be exactly equal.
- Use a dictionary to count the frequency of characters in one string and subtract the character frequencies from the second string. 
- If you encounter any character in the second string that isn't present in the dictionary, it can't be an anagram.
- Sum of frequencies in the dictionary after going through the second string should be 0 if it's an anagram.

**Time Complexity**

O(N) where N is the sum of length of the strings.

**Space Complexity**

O(N) since we go through every character in the strings constant number of times.

### [8. Binary search](https://leetcode.com/problems/binary-search/)

**Approach**

- check the middle index.
- if the target == middle, return the index.
- if target > middle, search the second half of the array.
- if target < middle, search the first half of the array.


**Time Complexity**

O(logN) since we reduce the search space by half in each iteration.

**Space Complexity**

O(1) since we don't use any extra space.


### [9. Flood fill](https://leetcode.com/problems/flood-fill/)

**Approach**

Standard DFS. Make sure to store the original color of a cell before filling it with new color.

**Time Complexity**

O(M * N) where the matrix is of dimension M x N since each cell is visited once.

**Space Complexity**

O(M * N) for recursion stack.


### [10. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

**Approach**

- Search on the left subtree if both p and q are smaller than root. 
- Search on the right subtree if both p and q are greater than root.
- return root otherwise (which means p & q are on either side of the root)

**Time Complexity**

O(N) where N = number of nodes in the tree. For balanced BST, it's O(logN)

**Space Complexity**

O(N)


### [11. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

**Approach**

- Compute height of left and right subtrees recursively.
- If at any node, the height differs by 1, return False. Otherwise, it's a balanced tree.

**Time Complexity**

O(N) where N = number of nodes in the tree since we encounter each node once.

**Space Complexity**

O(N)


### [12. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

**Approach**

- Fast and slow pointer.
- Move slow ptr by one step.
- Move fast ptr by two steps.
- If they meet, there's a cycle

**Time Complexity**

O(N) where N = number of nodes

**Space Complexity**

O(1)

### [13. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

**Approach**

- Use two stacks: one for pushing and one for popping.
- push():
    - insert to push-stack
- pop():
    - if pop-stack is non-empty, pop() from there.
    - otherwise, copy everything in reverse from the push stack into pop stack and pop()
- peek():
    - peek from the end of pop_stack if it's non-empty. Else, peek from the beginning of the push-stack if it's non-empty.
- empty():
    - true if both stacks are empty, false otherwise.

**Time Complexity**

- push(): O(1) 
- pop(): O(1) amortized.
- peek(): O(1)
- empty(): O(1)

**Space Complexity**

O(N)


### [14. First Bad Version](https://leetcode.com/problems/first-bad-version/)

**Approach**

Binary search. When a bad version is found, keep checking on the left half.

**Time Complexity**

O(logN)

**Space Complexity**

O(1)

### [15. Random Note](https://leetcode.com/problems/ransom-note/)

**Approach**

Use a freq counter.

**Time Complexity**

O(N) where N = max length of either words.

**Space Complexity**

O(1) since the size of the dictionary can be 26 characters max.

### [16. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

**Approach**

Similar to computing n-th fibonacci. Use a cache.

**Time Complexity**

O(N) since only N-1 recursive calls are needed due to caching.

**Space Complexity**

O(N) due to recursion stack.