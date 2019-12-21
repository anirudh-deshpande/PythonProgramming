class Solution(object):

    # takes 2^23 = 8388608 iterations
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        max_count = 0

        for i in range(1 << n):

            num_max = float('-inf')
            num_min = float('inf')

            count = 0

            for j in range(n):
                if i & (1 << j) != 0:
                    num_max = max(num_max, nums[j])
                    num_min = min(num_min, nums[j])

                    count += 1

            if num_max - num_min == 1:
                max_count = max(max_count, count)

        return max_count


    class Solution(object):

        # Takes 23 iterations
        def findLHS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """

            counter = {}

            for i in range(len(nums)):
                if nums[i] not in counter:
                    counter[nums[i]] = 0
                counter[nums[i]] += 1

            result = 0

            for key in counter:
                if key + 1 in counter:
                    result = max(result, counter[key] + counter[key + 1])

            return result

print Solution().findLHS([3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3])




