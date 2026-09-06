class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        target = 0
        for i, num in enumerate(nums):
            # sorted so first number pos then cant 0
            if nums[i]>0:
                break
            # Anchor might be dup
            if i >0 and nums[i]==nums[i-1]:
                continue
            # if its 0 or neg can zero proceed to do summing
            target = nums[i]
            right = len(nums)-1
            left = i+1
            while left<right:
                curr = nums[left]+nums[right]
                if curr+target==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif curr+target>0:
                    right-=1
                else:
                    left+=1
        return res
                
        