#!/usr/bin/env python3


# 调用字符串方法
print(message.title())
print(message.istitle())

first_name = "ada"
last_name = "lovelace"
# 在字符串中使用变量，可以在前引号加上字母f，再将要插入的变量放在花括号内，这样 python 显示字符串时将把每个变量都替换为其值，f 是 format 的简写
full_name = f"{first_name} {last_name}"
print(full_name)
# 对于 python 3.6 之前的版本，不支持上面写法，采用 format() 替代
print("{} {}".format(first_name, last_name))

# 使用制表符
print("Languages:\n\tPythonn\n\tJavaScript")

# 删除空白
favorite_language = "  python  "
print(f"-{favorite_language.rstrip()}-")
print(f"-{favorite_language.lstrip()}-")
print(f"-{favorite_language.strip()}-")

