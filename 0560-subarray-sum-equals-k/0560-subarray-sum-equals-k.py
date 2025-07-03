class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        hash_map[0] = 1
        count =  current_sum = 0
        for num in nums:
            current_sum += num
            remaning = current_sum - k
            if remaning in hash_map:
                count += hash_map[remaning]
            hash_map[current_sum] = hash_map.get(current_sum, 0) + 1
        return count
        


        