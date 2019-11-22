# 8.1 调用不需要变量的函数

# 8.1.1 变量 def f(x), p(x), 调用的时候，f(a)


def greet_user(username):
    """显示简单的问候语""" ## 注释问题，看一眼PEP 8
    print("Hello!")
    print("Hello, "+username.title()+"!")
greet_user('sarah')

# 8.2 f(x,y)

def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+"'s name is "+pet_name.title()+'.')

describe_pet('hamster','harry')
## 默认传递参数的顺序

describe_pet('dog','whillie')
## 函数嘛，定义一次之后，可以多次调用

describe_pet(animal_type='hamester',pet_name='harry')
## 可以指定给参数传递值，不用考虑顺序
describe_pet(pet_name='harry',animal_type='hamester')

# 设定参数默认值

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a "+animal_type+'.')
    print("My "+animal_type+"'s name is "+pet_name.title()+'.')

describe_pet(pet_name='whillie')
describe_pet(pet_name='yuanyuan',animal_type='panda')

# 参数不对劲的时候，会报错
# describe_pet()


# 8.3 返回值

## 返回一个字符串

def get_formatted_name(first_name, last_name):
    """返回姓名"""
    full_name= first_name+" "+last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

## 也许有的人有中间名，有的人没有，可选择性输入的参数

def get_formatted_name(first_name, last_name,middle_name=''):
    """返回姓名"""
    if middle_name:
        full_name= first_name+" "+middle_name+' '+last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('jimi','hendrix','lee')
print(musician)

# 返回字典

def build_person(first_name, last_name, age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)

# 结合函数使用while循环

def get_formatted_name(first_name, last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name=input("First name:")
    if f_name=='q':
        break

    l_name=input("Last name:")
    if l_name=='q':
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")

# 8.4 传递列表，就是你要给变量传递的值有一排

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)

usernames=['hanna','tw','we']
greet_users(usernames)


## 转移列表功能，抽象出来
unprinted_designs=['a','b','c','d']
completed_models=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()

    print("Printing model: "+current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

## 用两个函数实现列表转移功能

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# unprinted_designs=['a','b','c','d']
# # 创建一个列表，其中包含一些要打印的信息
# completed_models=[]

# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)
# show_completed_models(unprinted_designs)

## 如果不想掏空原来的列表，只想复制，那用切片进行引用
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs[:],completed_models)
show_completed_models(unprinted_designs)
show_completed_models(completed_models)
## 上面的操作要注释掉




# 8.5 任意数量的实参
def make_pizza(*toppings):
    print('我要一个酱婶儿的披萨'+str(toppings))
make_pizza('pepperoni')
make_pizza("mushrooms",'green peppers','extra cheese')

#for循环引入任意数量实参
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza("mushrooms",'green peppers','extra cheese')

#位置实参+任意数量实参,实际是元组参数
def make_pizza(size,*toppings):
    print('\nMaking a '+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#字典参数
def build_profile(first, last, **user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

# 8.6 将函数储存在模块中

#调用函数

import sys
sys.path.append("D:\Python练习") ## 一定要有这个！！！

import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(16,'pepperoni','green peppers','extra cheese')

#调用特定函数
import sys
sys.path.append("D:\Python练习") ## 一定要有这个！！！

from pizza import make_pizza as mp

mp(16,'pepperoni')

#给调用的模块指定名

import sys
sys.path.append("D:\Python练习") ## 一定要有这个！！！
import pizza as p
p.make_pizza(16,'pepperoni')

#导入模块中所有函数
import sys
sys.path.append("D:\Python练习")

from pizza import *
make_pizza(16,'pepperoni')
make_pizza(21,'mushrooms','green peppers','extra cheese')

# # 8.7 函数编写指南，看眼书，PEP 8
#

a='nihao'
help(a.title)
dir
In [ ]:
# 8-1 定义函数，调用函数

def display_message():
    print('颤抖吧函数，我来学你了哈哈哈哈！')

display_message()

# 8-2 喜欢的图书

def favorite_book(book):
    print(book+'这本书老好了，振聋发聩醍醐灌顶恍然大悟重新做人。')

favorite_book('道德经')

# 8-3 打印衬衫
def make_shirt(word,size):
    if size =='X':
        print(word)
        print('一起啃书')

    if size =='M':
        print(' -----_____----- ')
        print('|               |')
        print(' ---         ---')
        print('   |'+word+' !|   ')
        print('   |  一起啃书|   ')
        print('   |   ❥(^_-)|   ')
        print('    ---------    ')

    if size=='L':
        print(word)
        print('一起啃书')

make_shirt('奋发图强','X')
make_shirt(size='M',word='誓死不屈')

# 8-4

def make_shirt(size,word='我爱拍桑'):
    if size =='X':
        print(word)
        print('一起啃书')

    if size =='M':
        print(' -----_____----- ')
        print('|               |')
        print(' ---         ---')
        print('   |'+word+' !|   ')
        print('   |  一起啃书|   ')
        print('   |   ❥(^_-)|   ')
        print('    ---------    ')

    if size=='L':
        print(word)
        print('一起啃书')

make_shirt('M')
make_shirt('M','冲鸭冲鸭')

# 8-5
def describe_city(city,country='China'):
    print(city+'在'+country+'.')
describe_city('Hangzhou')
describe_city('zhuhai')
describe_city('gongzhufen')
describe_city('wangchuan','广莫之野无何有之乡')

# 8-6 返回值

def describe_city(city,country='China'):
    city_country=city+','+country
    return city_country

city_country_liaoning=describe_city('Liaoning')

print(city_country_liaoning)

# 8-7 返回字典

def make_album(singer,special_edition):
    music={}
    music['singer']=singer
    music['special_edition']=special_edition
    print(music)

make_album('周杰伦','依然范特西')
make_album('周杰伦','摩羯座')
make_album('致敬大神','一起啃书')

# 8-8 while

def make_album(singer,special_edition):
    music={}
    music['singer']=singer
    music['special_edition']=special_edition
    print(music)

print("输入你喜欢的歌手和专辑，输入't'随时退出")
while True:
    singer=input('你喜欢的歌手是谁？')
    if singer=='t':
        break
    else:
        special_edition=input('他有什么专辑？')
        if special_edition=='t':
            break
        else:
            make_album(singer,special_edition)

# 8-9 函数，功能是打印列表

def print_book_list(book_list):
    for book in book_list:
        print(book)

python_book_list=['Python编程从入门到实践','Python基础教程','Python语言及其应用']
print_book_list(python_book_list)

# 8-10 利用函数，对列表进行修改

def print_book_list(book_list):
    """打印列表"""
    for book in book_list:
        print(book)

def change_book_list(book_list):
    """修改列表"""
    n=0
    while n<len(book_list):
        book_list[n]='推荐：'+book_list[n]
        n+=1
    print_book_list(book_list)


python_book_list=['Python编程从入门到实践','Python基础教程','Python语言及其应用']

change_book_list(python_book_list)

# 8-11

def print_book_list(book_list):
    """打印列表"""
    for book in book_list:
        print(book)

def change_book_list(book_list):
    """修改列表"""
    n=0
    while n<len(book_list):
        book_list[n]='推荐：'+book_list[n]
        n+=1
    print_book_list(book_list)


python_book_list=['Python编程从入门到实践','Python基础教程','Python语言及其应用']

change_book_list(python_book_list[:])
print_book_list(python_book_list)


# 8-12 输入任意数量实参 三明治里加什么


def sandwich(*foods):
    print('您的要的三明治：')
    for food in foods:
        print('-'+food)

sandwich('guojiang','naiyou','huotui')

# 8-13

def build_profile(first, last, **user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile
wo=build_profile('zhijing','dashen',tezheng='mei',aihao='zhaojingzi')
print(wo)

# 8-14 自己定义一个字典 照上面抄就可以了

def cars(brand,type,**info):
    vehicle={}
    vehicle['牌子']=brand
    vehicle['型号']=type
    for key, value in info.items():
        vehicle[key]=value
    return vehicle

che=cars('aima','diandongche',daiyan='zhoujielun',yanse='fen')
print(che)

# 8-15 实现的功能就是函数导入 8.4.1的函数，


import sys
sys.path.append("D:\Python练习")

from printing_function import *

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

# printing_function.print_models(unprinted_designs[:],completed_models)
# printing_function.show_completed_models(unprinted_designs)
# printing_function.show_completed_models(completed_models)


print_models(unprinted_designs[:],completed_models)
show_completed_models(unprinted_designs)
show_completed_models(completed_models)



# 至 8-17