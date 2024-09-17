def find_pairs(nums, target):
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    
    return result

# 示例
nums = [2, 7, 11, 15, 3, 6]
target = 9
print(find_pairs(nums, target))  # 输出: [(2, 7), (3, 6)]