# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        idx = 0
        last_index = {}
        longest_length = 0
        
        for i, c in enumerate(s):
            if c not in last_index:
                last_index[c] = i
            else:
                if last_index[c] >= idx:
                    idx = last_index[c] + 1
                last_index[c] = i
                
            longest_length = max(longest_length, i - idx + 1)
            
        return longest_length

print(Solution().lengthOfLongestSubstring("abba"))