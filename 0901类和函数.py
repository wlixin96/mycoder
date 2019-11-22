# 理解什么是类，为什么会有类


# 9.1 创造和使用类

class Dog():  ### 首字母大写，不能使用下划线
    """一次模拟小狗的简单测试"""

    def __init__(self,name,age): # init自动变色，self必须有
        """初始化属性name和age"""
        self.name=name
        self.age=age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+' rolled over!')

my_dog= Dog('willie', 6)
a=my_dog.name
print(a)
my_dog.sit()
my_dog.roll_over()

print("My dog's name is "+my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+" years old.")

your_dog=Dog('lucy',3)
print("\nYour dog's name is "+your_dog.name.title()+'.')
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()



# 9.2 汽车类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

#加入带默认值得属性，直接修改，防止回调
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """打印一条指出汽车里程的消息"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")


    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles



my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()






# 9.3 继承
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """打印一条指出汽车里程的消息"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")


    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles

    def fill_gas_tank(self, gas):
        """汽车油箱还有多少油"""
        print('油箱还有：' + str(gas) + 'ml')



class ElectricCar(Car): # Car在前面，写在括号里
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        #super()是一个特殊的函数，调用父类属性
        self.battery_size=70

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a "+str(self.battery_size)+'-kWh battery.')

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
In [ ]:
# 9.2 汽车类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

#加入带默认值得属性，直接修改，防止回调
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """打印一条指出汽车里程的消息"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")


    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles



my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
In [ ]:
# 9.3 继承
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """打印一条指出汽车里程的消息"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")


    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles

    def fill_gas_tank(self, gas):
        """汽车油箱还有多少油"""
        print('油箱还有：' + str(gas) + 'ml')



class ElectricCar(Car): # Car在前面，写在括号里
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        #super()是一个特殊的函数，调用父类属性
        self.battery_size=70

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a "+str(self.battery_size)+'-kWh battery.')

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print('俺们电动汽车没有油箱')


my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 9.3.4 重写父类 直接加定义函数
my_tesla.fill_gas_tank()
In [ ]:
# 实例作为属性，在类函数里面引用一个类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车描述的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return  long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        """打印一条指出汽车里程的消息"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot roll back an odometer")


    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles



class Battery():
    """一次模拟电动汽车电瓶的简化尝试"""

    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)


        self.battery=Battery()

my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
In [ ]:
# 9.4 导入类
import sys
sys.path.append("D:\Python练习")

from car import Car

class Battery():
    """一次模拟电动汽车电瓶的简化尝试"""

    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270



        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)


        self.battery=Battery()

my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 9.4.3 从一个模块导入多个类

import sys
sys.path.append("D:\Python练习")
from car_electriccar import Car,ElectricCar


my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




# 9.4.4 或者直接导入模块，用.去引用具体类，推荐使用这种方法

import sys
sys.path.append("D:\Python练习")
import car_electriccar


my_tesla=car_electriccar.ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.4.5 导入所有类，不推荐，能看懂就行了,类名称容易冲突

import sys
sys.path.append("D:\Python练习")
from car_electriccar import *

my_tesla=ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 9.4.6 一个模块引入

import sys
sys.path.append("D:\Python练习")

from car import Car
from electriccar import ElectricCar

my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.5 Python标准库，从模块collection中导类

from collections import OrderedDict

favorite_languages=OrderedDict()
##创建一个空的有序字典

favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+'.')

# 9.6 字典编码风格 大写不能有下划线 文档字符串

# class Dog

# def_1

# def_2

# Class_1


# Class_2

## import 导入，先导入标准库

## import 自定义模块中的类
In [ ]:
# 9-1

class Restaurant(): ##啊啊大小写啊，class小写，R大写
    """模拟饭店调查"""

    def __init__(self,restaurant_name,cuisine_type):
        # 不要忘记def空格__两个下划线
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self): #不要忘记这个self
        print(self.name+'的'+self.type+'很不错')

    def open_restaurant(self):
        print('而且他正在营业')
        ## 内部参数，不要忘了self

restaurant=Restaurant('杨国福','麻辣烫')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2

restaurant_1=Restaurant('马景涛','麻辣烫')
restaurant_1.describe_restaurant()

restaurant_2=Restaurant('新玛特','麻辣烫')
restaurant_2.describe_restaurant()

restaurant_3=Restaurant('国泰','麻辣烫')
restaurant_3.describe_restaurant()

# 9-3

class User():
    """记录用户信息"""

    def __init__(self,xing,ming,*qita):
        self.xing=xing
        self.ming=ming
        self.qita=qita

    def describe_user(self):
        print("姓："+self.xing)
        print("名："+self.ming)
        if self.qita:
            print('\n其他：\n')
            for info in self.qita:
                print("-"+info)

    def greet_user(self):
        print('\n'+self.ming + '仔,我们奈你！')
        print(self.ming+'仔,你老霸道了！')

zjds=User('致敬大',
          '神',
          '美','帅呆','机智','成功')

zjds.describe_user()
zjds.greet_user()

# 9-4 加入就餐人数

class Restaurant():
    """模拟饭店调查"""

    def __init__(self,restaurant_name,cuisine_type):
        # 不要忘记def空格__两个下划线
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0

    def describe_restaurant(self): #不要忘记这个self
        print(self.name+'的'+self.type+'很不错')

    def open_restaurant(self):
        print('而且他正在营业')
        ## 内部参数，不要忘了self

    def set_number_served(self,number):

        if number>=self.number_served:
            self.number_served=number

        print('共有'+str(self.number_served)+'人在此用餐过。')

    def increment_number_served(self,increment_number):
        self.number_served+=increment_number
        print('共有' + str(self.number_served) + '人在此用餐过。')


restaurant=Restaurant('杨国福','麻辣烫')
restaurant.set_number_served(100)
restaurant.increment_number_served(50)

# 9-5 尝试登陆次数

class User():
    """记录用户信息"""

    def __init__(self,xing,ming,*qita):
        self.xing=xing
        self.ming=ming
        self.qita=qita
        self.login_attempts=0

    def describe_user(self):
        print("姓："+self.xing)
        print("名："+self.ming)
        if self.qita:
            print('\n其他：\n')
            for info in self.qita:
                print("-"+info)

    def greet_user(self):
        print('\n'+self.ming + '仔,我们奈你！')
        print(self.ming+'仔,你老霸道了！')

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

    def print_login_attempts(self):
        print('您登陆了'+str(self.login_attempts)+'次')


zjds=User('致敬大',
          '神',
          '美','帅呆','机智','成功')

zjds.increment_login_attempts()
zjds.increment_login_attempts()
zjds.increment_login_attempts()
zjds.print_login_attempts()
zjds.reset_login_attempts()
zjds.print_login_attempts()



# 9-6 继承Restaurant

class Restaurant():
    """模拟饭店调查"""

    def __init__(self,restaurant_name,cuisine_type):
        # 不要忘记def空格__两个下划线
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0

    def describe_restaurant(self): #不要忘记这个self
        print(self.name+'的'+self.type+'很不错')

    def open_restaurant(self):
        print('而且他正在营业')
        ## 内部参数，不要忘了self

    def set_number_served(self,number):

        if number>=self.number_served:
            self.number_served=number

        print('共有'+str(self.number_served)+'人在此用餐过。')

    def increment_number_served(self,increment_number):
        self.number_served=increment_number
        print('共有' + str(self.number_served) + '人在此用餐过。')

class IceCreamStand(Restaurant):
    """继承9-4，冰淇淋特殊餐馆"""

    def __init__(self,restaurant_name,cuisine_type):

        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['vanilla','chocolate','durian',]

    def print_flavors(self):
        print("\n")
        for flavor in self.flavors:
            print(flavor)

restaurant_4=IceCreamStand('麦当劳甜品站','冰淇淋')
restaurant_4.print_flavors()

# 9-7 继承User，管理员

class User():
    """记录用户信息"""

    def __init__(self,xing,ming,*qita):
        self.xing=xing
        self.ming=ming
        self.qita=qita

    def describe_user(self):
        print("姓："+self.xing)
        print("名："+self.ming)
        if self.qita:
            print('\n其他：\n')
            for info in self.qita:
                print("-"+info)

    def greet_user(self):
        print('\n'+self.ming + '仔,我们奈你！')
        print(self.ming+'仔,你老霸道了！')

class Admin(User):
    """特殊的用户，管理员"""

    def __init__(self,xing,ming,*qita):

        super().__init__(xing,ming,*qita)
        self.privileges='和稀泥'

    def show_privileges(self):
        print('\n管理员能'+self.privileges)


zjds=Admin('致敬大',
          '神',
          '美','帅呆','机智','成功')

zjds.show_privileges()

# 9-8 权限



class User():
    """记录用户信息"""

    def __init__(self,xing,ming,*qita):
        self.xing=xing
        self.ming=ming
        self.qita=qita

    def describe_user(self):
        print("姓："+self.xing)
        print("名："+self.ming)
        if self.qita:
            print('\n其他：\n')
            for info in self.qita:
                print("-"+info)

    def greet_user(self):
        print('\n'+self.ming + '仔,我们奈你！')
        print(self.ming+'仔,你老霸道了！')

class Admin(User):
    """特殊的用户，管理员"""

    def __init__(self,xing,ming,*qita):

        super().__init__(xing,ming,*qita)


    def show_privileges(self):
        Privileges()

class Privileges():
    """管理人员特权"""

    def __init__(self):
        self.privileges = '和稀泥'
        print('\n管理员能' + self.privileges)


zjds=Admin('致敬大',
          '神',
          '美','帅呆','机智','成功')

zjds.show_privileges()


# 9-9 电瓶升级
import sys
sys.path.append("D:\Python练习")

import car_electriccar

new_car=car_electriccar.ElectricCar('aima','A4','2013')
new_car.battery.upgrade_battery()
new_car.battery.get_range()

# 9-10 导入Restaurant

import sys
sys.path.append("D:\Python练习")

import restaurant

r=restaurant.Restaurant('杨国福','麻辣烫')
r.describe_restaurant()
r.open_restaurant()

# 9-11 导入Admin，调用9-8的程序

import sys
sys.path.append("D:\Python练习")

import admin

zjds=admin.Admin('致敬大','神','美','帅呆','机智','成功')

zjds.show_privileges()

# 9-12 导入多个模块


import sys
sys.path.append("D:\Python练习")

import admin_import_user

zjds=admin_import_user.Admin('致敬大','神','美','帅呆','机智','成功')

zjds.show_privileges()

# 9-13 OrderDict,重写6-4
## 习题6-3,6-4粘贴过来
python_words={'Code lay out':'代码布局',
              'Whitespaces in Expressions':'表达式中的空格',
              'Comments':'注释',
              'Naming Conventions':'命名规范',
              'programming recommendations':'编程建议',
              'Global Variable Names':'全局变量名',
              'Function Annotation':'功能注释',
              'Indentation':'缩进',
              'Binary Operator':'运算符',
              'String quotes':'字符串引号'
              }

for word, explaination in python_words.items():
    print("\n"+word+":")
    print(explaination)

## 改写
from collections import OrderedDict

python_words = OrderedDict()

python_words['Code lay out']='代码布局'
python_words['Whitespaces in Expressions']='表达式中的空格'
python_words['Comments']='注释'
python_words['Naming Conventions']='命名规范'
python_words['String quotes']='字符串引号'

n=0
for word, explaination in python_words.items():
    print("\n"+str(n)+' '+word+":")
    print(explaination)
    n+=1

# 9-14 随机数模拟骰子

from random import randint

##测试一下这个函数的功能
x = randint(1,6) #闭区间
print(x)
x = randint(1,6)
print(x)
x = randint(1,6)
print(x)

from random import randint
x = randint(1,6)
print(x)
print(x)
print(x)

## 定义一个类，x个面的筛子掷n次

from random import randint
class Die():

    def __init__(self,sides):
        self.sides=sides

    def roll_die(self):
        self.side=randint(1,self.sides)
        print(self.side)

    def roll_die_times(self,times):

        self.n=0
        self.times=times
        while self.n<self.times:
            self.roll_die()
            self.n+=1

x=Die(6)
x.roll_die_times(10)

y=Die(10)
y.roll_die_times(5)

z=Die(20)
z.roll_die_times(10)

#9-15 Python Module of the Week https://pymotw.com/3/