class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        print(len(numbers)) #4
        while(left<right):
            sum = numbers[right]+numbers[left]
            if sum == target:
                return [left+1,right+1]
            if sum>target:
                right-=1
            if sum<target:
                left+=1
        return []