def harmonic_mean(nums):
    """Computing the harmonic mean"""
    return len(nums) / sum(1 / num for num in nums)
