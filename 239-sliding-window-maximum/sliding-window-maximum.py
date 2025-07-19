from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove from front if outside window
            if q and q[0] <= i - k:
                q.popleft()

            # Remove smaller values from back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Append max once we reach window size
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
