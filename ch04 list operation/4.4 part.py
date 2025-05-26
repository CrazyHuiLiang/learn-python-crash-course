
players = ['charles', 'martin', 'michael', 'florence', 'eli']

# 返回索引 0 到 3 之间的元素
print(players[0:3])
# 返回前4 个元素
print(players[0:4])

# 返回从第3 个元素开始到末尾的元素
print(players[2:])

# 返回从最后 2 个元素
print(players[-2:])

# 复制列表
my_players = players[:]
players.append('wang')
my_players.append('zhang')
print(players)
print(my_players)


