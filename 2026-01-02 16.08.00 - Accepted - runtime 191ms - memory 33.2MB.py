class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # (value, steps to remove this element)
        result = 0
        
        for i in range(n - 1, -1, -1):
            steps = 0
            while stack and nums[i] > stack[-1][0]:
                steps = max(steps + 1, stack[-1][1])
                stack.pop()
            stack.append((nums[i], steps))
            result = max(result, steps)
        
        return result