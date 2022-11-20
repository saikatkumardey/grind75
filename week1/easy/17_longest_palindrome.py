class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_counter = {}
        for char in s:
            freq_counter[char] = freq_counter.get(char,0) + 1
        odd_found = 0
        for char,freq in freq_counter.items():
            if freq%2 == 1:
                freq_counter[char] -= 1
                odd_found = 1
        return sum(freq_counter.values()) + odd_found
    