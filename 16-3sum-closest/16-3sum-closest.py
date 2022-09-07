class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            while l<r:
                dummy = nums[l] + nums[r] + nums[i]
                if dummy == target:
                    return dummy
                if abs(dummy-target) < abs(result-target):
                    result = dummy
                if dummy<target:
                    l += 1
                elif dummy>target:
                    r -= 1
        return result