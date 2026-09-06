class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(numbers):
            des = target-num
            if des in map:
                return [map[des]+1,i+1];
            map[num]=i
        return []