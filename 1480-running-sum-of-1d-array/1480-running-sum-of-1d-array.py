class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for num in range(len(nums)):
            sum = 0
            for i in range(num+1):
                sum += nums[i]
            sums.append(sum)
        return sums
        