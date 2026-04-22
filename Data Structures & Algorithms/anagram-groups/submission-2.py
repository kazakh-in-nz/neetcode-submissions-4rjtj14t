class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        
        for s in strs:
            # Count character frequencies
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Use tuple as key (hashable)
            key = tuple(count)
            
            # Group by key
            if key not in m:
                m[key] = []
            m[key].append(s)
        
        return list(m.values())