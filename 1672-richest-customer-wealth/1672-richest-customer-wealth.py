class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = []
        for i in range(len(accounts)):
            s = 0
            for j in range(len(accounts[i])):
                s += accounts[i][j]
            result.append(s)
        return max(result)
        