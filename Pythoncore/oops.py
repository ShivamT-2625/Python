nums = [7,9,3,5,0]

def solution(nums):
    if not nums:
        return None
    nums_sorted = sorted(nums)
    return nums_sorted[-2]
print(solution(nums))