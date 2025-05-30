
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# Add new key-value pairs
alien_0['x_position'] = 0

# Delete key-value pairs
del alien_0['points']
print(alien_0)

# 多行赋值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

# get()  方法
print(favorite_languages.get('erin', 'No poll yet.'))

# 遍历字典
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# keys()  方法
for  name in favorite_languages.keys():
    print(name.title())

# for in 默认会遍历字典的 key
for  name in favorite_languages:
    print(name.title())

# sorted() 方法
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# values() 方法
for language in favorite_languages.values():
    print(language.title())

