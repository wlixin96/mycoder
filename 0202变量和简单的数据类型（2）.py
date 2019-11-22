#删除空白，暂时删除字符串末尾的空白
favorite_language='python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

#永久删除字符串末尾的空白
favorite_language='python '
favorite_language=favorite_language.rstrip()
print(favorite_language)

#删除字符串开头的空白
favorite_language=' python'
print(favorite_language.lstrip())
print(favorite_language)

#删除开头、末尾、两端空白函数
favorite_language=' a '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#数字
a=2+3
b=3-2
c=2*3
d=3/2
e=3**2 #3的二次方
f=(2+3)*4
print(a,b,c,d,e,f)

#浮点数
a=0.1+0.1
b=0.2+0.2
c=2*0.1
d=2*0.2
print(a,b,c,d)

#数值转化为字符串str（）函数
age=23
message='happy '+str(age)+'rd Birthday'
print(message)
import this

# 2-1 信息储存到变量，将其打印出来
a="I love you 3000 times"
print(a)

# 2-2 修改变量，再打印
a='lalala逗你玩'
print(a)
a='heiheihei不逗你啦'
print(a)

# 2-3个性化消息
a='Eric'
print('Hello '+a+', would you like to learn some Python today?')

# 2-4 人名，小写、大写，首字母大写的方式显示
a='Mary antoine'
print(a.lower())
print(a.upper())
print(a.title())

# 2-5 双引号
print('Shakespeare thus said: "Love all, trust a few, do wrong to none."')

# 2-6 重复2-5，变量message，变量famous_people
famous_people='Shakespeare '
message='thus said: "Love all, trust a few, do wrong to none."'
print('\n'+famous_people+message)

# 2-7 \t,\n,打印这个人名，lstrip,rtrip,trip
famous_people='\tShakespeare\t\t\n '
print(famous_people)
a=famous_people.lstrip()
print(a)
b=famous_people.rstrip()
print(b)
c=famous_people.strip()
print(c)
# 2-8 加减乘除=8
print(3+5)
print(9-1)
print(4*2)
print(16/2) #神奇，小数点为啥会保留一位
print(2**3)

# 2-9
a=666
print(str(a)+' is my favourite number')
print(a.__str__()+' is my favourite number')
# 2-10 添加注释

# 2-11 Python之禅
import this # 不能重复导入这个模块why？