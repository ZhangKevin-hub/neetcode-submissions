class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)  # Strips all duplicates in O(N) time
        longest = 0
        
        for n in num_set:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                
                # Count consecutive values upwards
                while (n + length) in num_set:
                    length += 1
                    
                longest = max(longest, length)
                
        return longest