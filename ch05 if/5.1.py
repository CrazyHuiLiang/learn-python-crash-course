
car = "Audi"
if car == "Audi":
    print("This is Audi")
elif car == "BMW":
    print("This is BMW")
elif car == "Mercedes":
    print("This is Mercedes")
else:
    print("This is not Audi, BMW or Mercedes")


age1 = 18
age2 = 20
# 多个条件满足
if age1 >= 18 and age2 >= 18:
    print("Both are above 18")

# 满足一个条件
if age1 >= 18 or age2 >= 18:
    print("One of them is above 18")

# 检查特定值是否在列表中
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")

# 检查特定值是否不在列表中
requested_topping = ['mushrooms', 'extra cheese']
if 'pepperoni' not in requested_topping:
    print("Sorry, we are out of pepperoni.")



