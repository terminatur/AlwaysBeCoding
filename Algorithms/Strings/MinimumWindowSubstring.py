# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


from collections import deque
from typing import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for c in t:
            if c not in t_counts:
                t_counts[c] = 1
            else:
                t_counts[c] += 1
                
        left = 0
        right = 0
        min_left = None
        min_right = None
        
        window = deque()
        window_counts = {}
        
        for i, c in enumerate(s):
            right += 1
            if c not in t_counts:
                continue
            
            if c not in window_counts:
                window_counts[c] = 1
            else:
                window_counts[c] += 1
                
            window.append((c, i))
            
            while len(window) > 0 and window_counts[window[0][0]] > t_counts[window[0][0]]:
                e, it = window.popleft()
                window_counts[e] -= 1
            left = window[0][1]
                
            if min_left is None:
                all_chars_present_in_window = True
                for e in t_counts:
                    if e not in window_counts:
                        all_chars_present_in_window = False
                        break
                    if window_counts[e] < t_counts[e]:
                        all_chars_present_in_window = False
                        break
                if all_chars_present_in_window:
                    min_left = left
                    min_right = right
            else:
                if right - left < min_right - min_left:
                    min_left = left
                    min_right = right
                    
        if min_left is None:
            return ""
        else:
            return s[min_left:min_right]
                    
                
s = "a"
t = "a"
print(Solution().minWindow(s, t))
