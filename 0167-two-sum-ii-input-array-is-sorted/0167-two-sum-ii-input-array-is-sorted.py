class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in memo:
                return [memo[remainder]+1,i+1]
            memo[numbers[i]] = i
        return [-1,-1]