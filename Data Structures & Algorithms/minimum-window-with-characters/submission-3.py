class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        have = 0
        required = len(need)

        left = 0
        best = ""

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
        
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                window_len = right - left + 1
                if not best or window_len < len(best):
                    best = s[left:right + 1]
                
                left_c = s[left]
                window[left_c] -= 1

                if left_c in need and window[left_c] < need[left_c]:
                    have -=1
                
                left += 1
        
        return best