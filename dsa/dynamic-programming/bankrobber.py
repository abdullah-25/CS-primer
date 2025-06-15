def bank_robber_top_down(nums):
    cache = {}
    def dp(i):
        if i >= len(nums):
            return 0
        if i in cache:
            return cache[i]

        curr = nums[i] + dp(i+2)
        skip = dp(i+1)

        cache[i] = max(curr, skip)
        return cache[i]
    return dp(0)

def bank_robber_bottom_up(nums):
    prev, prev_prev = 0,0
    for n in nums:
        prev, prev_prev = max(n+prev_prev, prev), prev
    return prev