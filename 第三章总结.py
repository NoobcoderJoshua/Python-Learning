#列表的使用
#列表的生成
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素
print(bicycles[0])#打印访问的第一个列表元素
print(bicycles[0].title())#整理格式

#索引从0而不是1开始
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])
#特殊语法：将索引指定为-1，访问列表最后一个元素
print(bicycles[-1])

#使用列表中的各个值
message = "My first bicycle was a "+bicycles[0].title()+"."
print(message)

#修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#在列表中添加元素
##在列表末尾添加元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

###在列表中插入元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')#在第一个元素位置插入ducati
print(motorcycles)

#从列表中删除元素:使用del语句。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#使用pop语句删除元素（元素可继续被使用）
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()#弹出最顶层的一个元素，即suzuki，并且该被弹出元素的值赋入另一个变量popped_motorcycles，可以接下来继续使用它
print(motorcycles)
print(popped_motorcycles)
#使用pop()弹出列表任何位置处的元素
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title()+'.')

#根据值删除元素（元素也可被继续使用）
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')#该语句只删除第一个值，如要删除所有的相同值，需要使用循环语句
print(motorcycles)

#组织列表
##使用方法sort对列表进行永久性排列
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)#这种方法使得该列表元素按照字母顺序排列,而且是永久的
cars.sort(reverse=True)
print(cars)#向sort传递reverse=True参数，可以让列表元素按照字母顺序的相反方向排列

#使用函数sorted对列表进行临时排序
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

#获取列表长度
print(len(cars))

