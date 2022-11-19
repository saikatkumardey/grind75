class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq_magazine = {}
        for char in magazine:
            freq_magazine[char] = freq_magazine.get(char, 0) + 1

        for char in ransomNote:
            char_freq_in_magazine = freq_magazine.get(char, 0)
            if char_freq_in_magazine == 0:
                return False
            freq_magazine[char] -= 1

        return True
