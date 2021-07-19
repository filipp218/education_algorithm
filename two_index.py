class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        let_in_seq = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            elem = s[i]
            if elem in let_in_seq:
                start = max(start, let_in_seq[elem] + 1)
            max_len = max(i - start + 1, max_len)
            let_in_seq[elem] = i
            
        return max_len
