class Solution(object):
    def subsets(self, nums):
        result = []
        path = []

        def backtrack(index):
            if index == len(nums):
                result.append(path[:])
                return

            # Include nums[index]
            path.append(nums[index])
            backtrack(index + 1)

            # Don't include nums[index]
            path.pop()
            backtrack(index + 1)

        backtrack(0)
        return result