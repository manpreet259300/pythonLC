# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def find3sum(nums, output):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        head = i + 1
        end = n - 1
        while head < end:
            print("head = ", nums[head], " end = ", nums[end], " I = ", nums[i])
            if nums[head] + nums[end] + nums[i] == output:
                result.append([nums[i], nums[head], nums[end]])
                head = head + 1
                while head < end and nums[head] == nums[head - 1]:
                    head = head + 1
            elif nums[head] + nums[end] + nums[i] > output:
                end = end - 1
            else:
                head = head + 1

    print(result)
    return result


nums = [-1, 0, 1, 2, -1, -4]
output = 0

result = find3sum(nums, output)
