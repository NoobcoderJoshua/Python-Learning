#if语句
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
	    print(car.upper())
	else:
		print(car.title())
#条件测试
#检查两个值是否相等
car = 'bmw'
print(car == 'bmw')#如果car = 'bmw'，则为True，反之为False

##注意大小写不同的值会被视作不相等
car = 'Audi'
print(car == 'audi')#结果为false

#检查两个值是否不等
a='mushroom'
if a != 'anchovies':
	print("Hold the anchovies!\n")

#比较数字:方法如上
age = 19
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)

#and和or
age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1>= 21) #and类似于数学的交集
age_1 = 22
print(age_0 >= 21 and age_1 >=21)

age_0 = 22
age_1 = 18
age_0 >=21 or age_1 >= 21
age_0 = 18
age_0 >= 21 or age_1>=21#or类似于数学中的并集

#还可以检查特定值是否在列表中
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print(user.title()+"you can post a respone if you wish")

#if语句系列
#if-else语句
age = 17
if age>= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote")
	print("please register to vote as soon as you turn 18!")


#多条件情况下，运用if-elif-else结构
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
#直到满足条件才会执行
#还可以利用变量，将判断条件设为price，打印的内容包含变量。
#有时可以省略else（elif代替else）



#多个if语句串联的情况：测试多个条件。因为在第一个通过测试的条件之后的其他测试和指令将不执行。

#检查列表特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':#检查顾客订单（检查青椒是否存在）
		print("sorry, we are out of green peppers right now.")
	else:
		print('Adding '+ requested_topping + ".")
print("\nFinished making your pizza!")

#确定列表是否为空
requested_toppings = []
if requested_toppings:#列表名作为条件：检查是否为空列表---返回为True和False
	for requested_topping in requested_toppings:
		print("Adding "+ requested_topping + ".")
	print("\nFinished making your Pizza!")
else:
	print("Are you sure you want a plain pizza?")#检查到空列表时的执行操作
#使用多个列表
#检查是否有交集元素:使用in
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:#注意是requested_topping不是requested_toppings
		print('Adding ' + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinshed making your pizza!")


