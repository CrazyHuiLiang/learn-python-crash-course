#!/usr/bin/env python3

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改数组中的元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素
motorcycles.append('honda')
print(motorcycles)

# 插入元素
motorcycles.insert(0, 'honda')
print(motorcycles)

# 使用 del 删除元素
del motorcycles[0]
print(motorcycles)

# 使用 pop() 删除元素
popped_value = motorcycles.pop()
print(motorcycles)
print(popped_value)

# 对列表排序
motorcycles.sort()
print(motorcycles)
# 对列表按字母逆向排序
motorcycles.sort(reverse=True)
print(motorcycles)

# 使用 sorted() 函数对列表进行临时排序
print(sorted(motorcycles))
print(motorcycles)

# 翻转列表
motorcycles.reverse()
print(motorcycles)

#  确定列表的长度
print(len(motorcycles))
