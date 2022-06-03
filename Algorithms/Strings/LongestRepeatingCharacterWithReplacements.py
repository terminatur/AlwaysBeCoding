# Leetcode #424

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_idx = {}
        replacement_idx = {}
        longest_length = 0
        
        for i, c in enumerate(s):
            if c not in char_idx:
                char_idx[c] = deque()
                replacement_idx[c] = deque()
            char_idx[c].append(i)

            longest_length = max(longest_length, len(char_idx[c]) + len(replacement_idx[c]) + (k - len(replacement_idx[c])))
            
            # iterate over last k chars since they could add a replacement char
            start = max(0, i - k)
            for r in range(start, i):
                revisit_char = s[r]
                if revisit_char != c:
                    # have to increment the replacement
                    if len(replacement_idx[revisit_char]) == 0 or replacement_idx[revisit_char][-1] != i:
                        replacement_idx[revisit_char].append(i)
                    if len(replacement_idx[revisit_char]) > k:
                        while char_idx[revisit_char][0] < replacement_idx[revisit_char][0]:
                            char_idx[revisit_char].popleft()
                            
                    longest_length = max(longest_length, len(char_idx[revisit_char]) + len(replacement_idx[revisit_char]) + (k - len(replacement_idx[revisit_char])))
                    
            
            
        return min(longest_length, len(s))

print(Solution().characterReplacement("AABA", 0))
# "AABABBA"
# 1
