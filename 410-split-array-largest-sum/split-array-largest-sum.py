class Solution(object):
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            subarr = 1
            currentsum = 0

            for num in nums:
                if currentsum + num > mid:
                    subarr += 1
                    currentsum = num
                else:
                    currentsum += num

            if subarr <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left