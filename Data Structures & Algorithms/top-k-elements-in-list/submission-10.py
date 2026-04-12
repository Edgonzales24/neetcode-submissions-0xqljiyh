class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = {} # num : count
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for n, i in count.items():
            freq[i].append(n)
        
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
