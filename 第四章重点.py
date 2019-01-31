#for循环
magicians = ['alice','david','carolina']
for magician in magicians:#注意不要遗漏冒号
	print(magician)#获取元素——储存到新变量中——打印
for magician in magicians:	
    print(magician.title()+',that was a great trick!')
    #问题：如果本句中print不再缩进，打印结果只会显示Carolina,that was a great trick!（P48）,print只在循环结束后执行一次这是一个逻辑错误
for magician in magicians:	
    print(magician.title()+',that was a great trick!')
    print("I can't wait to see you next trick, "+ magician.title()+".\n")
#注意缩进错误：忘记缩进和多余缩进

#创建数值列表
##使用函数range()
for value in range(1,5):
	print(value)#由于差一行为，在到达4后执行停止。故只会打印数字1——4
#所以要打印数字1——5，就应当使用
for value in range(1,6):
	print(value)
	
#使用list将range的结果直接转为列表。
numbers = list(range(1,6))
print(numbers)
#使用range指定步长。（如打印1~10内的偶数）
even_numbers = list(range(2,11,2))
print(even_numbers)
#乘方运算表示例
#创建一个空列表
#for value in range(1,11):
#	square = value**2
#n=list(str(square))
#print(n)
#以上为什么不可以？
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)#官方解法

#几个简单的统计函数
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
#####################################################
print('\n')

#切片和遍历切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])#注意是冒号#提取列表第2-4个元素
print(players[:4])#从列表开头提取到第四个元素
print(players[2:])
print(players[-3:])#打印最后三个元素
##遍历切片
players = ['charles','martina','michael','florence','eli']
print('here are the first three players on my team：')
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are")
print(friend_food)

#复制列表情况二
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods[:]
my_foods.append('cannoli')
friend_food.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_food)
############################################################


#元组：不可变的列表
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#遍历元组中所有值
for dimension in dimensions:
	print(dimension)
#############
#修改元组变量
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
print("\nmodified dimensions:")
for dimension in dimensions:
	print(dimension)
