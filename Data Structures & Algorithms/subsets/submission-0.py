class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        substack = []

        def dfs(i):
            if i >= len(nums):
                res.append(substack.copy())

                return

            substack.append(nums[i])
            dfs(i+1)
            substack.pop()
            dfs(i+1)
        dfs(0)
        return  res