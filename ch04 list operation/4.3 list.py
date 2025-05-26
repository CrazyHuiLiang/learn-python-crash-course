
# 使用 range() 创建数字列表 1到 4
for value in range(1, 5):
    print(value)

# 可以使用 list() 函数将 range() 创建的数字列表转换为列表
numbers = list(range(1, 6))
print(numbers)

# ** 表示乘方运算
for value in range(1, 6):
    print(value**2)

# 统计计算
digits = list(range(1, 10))
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

