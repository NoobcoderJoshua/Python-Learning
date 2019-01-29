#对变量的处理#
name = "ada lovelace"
print(name.upper())
print(name.lower())
print(name.title())      #除此之外，还有使用+号合并字符串的方法，使用""来插入空白

#对字符串的处理(Q：这些对变量如何使用？）
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
#\n\t可以使插入制表符和换行的效果同时出现

#删除空白
favorite_language = 'python '
print(favorite_language + "A")
print(favorite_language.rstrip() + "A")
#rstrip为暂时删除

#完全删除：需要存回原来变量中
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language + 'A')

#其他空白剔除形式
favorite_language = ' python '
print(favorite_language.rstrip() + 'A')#删掉后空白
print(favorite_language.lstrip() + 'A')#删掉前空白
print(favorite_language.strip() + 'A')#删掉双侧空白

#将非字符串值表示为字符串
age = 23
message = 'Happy ' + str(age) + 'rd Bithday!'
print(message)#关于对int和str使用区别的理解，对非字符串值和字符串差别的理解；

#运算大全
#整数运算
print(2+3)#加法
print(3-2)#减法
print(2*3)#乘法
print(3/2)#除法
print(3**2)#乘方运算
print((2+3)*4)#运算顺序
print(0.1+0.1)#浮点数

