class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        d = {0: 1}

        for x in nums:
            prefix += x

            if prefix - k in d:
                count += d[prefix - k]

            d[prefix] = d.get(prefix, 0) + 1

        return count