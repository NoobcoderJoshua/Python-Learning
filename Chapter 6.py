#字典的使用
#一个简单的字典
alien_0 = {'color':'green','points' : 5}#该字典储存了外星人的颜色和点数信息
print(alien_0['color'])
print(alien_0['points'])
#字典是一系列键——值对。

#访问字典中的值
new_points = alien_0['points']
print("You just earned " + str(new_points)+" points")

#添加键——值对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#先创建空字典再添加值
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值:重新定义

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+ str(alien_0['x_position']))
#向右移动外星人
#根据外星人速度决定移动多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3#外星人移动速度特别快
alien_0['x_position'] = alien_0['x_position'] + x_increment#新位置等于老位置+增量（increment）
print("New x-position: " + str(alien_0['x_position']))

#删除键——值对
#使用del语句删除
alien_0 = {'color': 'green', "points":5}
print(alien_0)

del alien_0['points']
print(alien_0)
#删除的键——值对永远消失了

favorite_languages = {
	'jen': 'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
print("Sarah's favorite language is "+ 
	favorite_languages['sarah'].title()+
	".")

#遍历字典
#有很多方式：遍历字典的键——值对，遍历字典的键，遍历字典的值。
user_0 = {
	'username': 'efermi',
	'first':'enrico',
	'last':'fermi',
	}
for key, value in user_0.items():#声明两个变量:键和值，key,value或k,v
	print("\nKey: " + key)
	print("Value: " + value)
#或者把key和value换为其他，效果相同
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

#遍历字典中的所有键：
for name in favorite_languages.keys():
	print(name.title())
#由于遍历字典时会默认遍历所有的键，因此，这样写的效果同上：
for name in favorite_languages:
	print(name.title())
	
	
#使用当前键来访问与之相关联的值
favorite_languages = {
	'jen': 'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	
if name in friends:
	print(" Hi " + name.title()+ 
	", I see your favorite language is " +
	favorite_languages[name].title() + "!")

#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll!")

#按顺序遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

#嵌套
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)
