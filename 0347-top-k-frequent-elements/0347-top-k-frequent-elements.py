class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        ctr = 0
        
        uniq_nums = list(set(nums))
        
        for num in uniq_nums:
            count[num] = nums.count(num)
        
        count = dict(sorted(count.items(), key = lambda count:count[1],reverse=True))
        
        for key in count:
            if ctr == k:
                return res
            res.append(key)
            ctr += 1
        
        return res