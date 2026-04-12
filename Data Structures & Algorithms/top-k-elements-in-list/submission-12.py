class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # nums: count
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res