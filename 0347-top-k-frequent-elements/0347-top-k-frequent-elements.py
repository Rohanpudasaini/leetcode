class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        final_result = []
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        for key, cnt in hash_map.items():
            final_result.append([cnt, key])
        final_result.sort()
        result = []
        while len(result) < k:
            result.append(final_result.pop()[1])
        return result 