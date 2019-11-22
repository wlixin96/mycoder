#0402 第四章的习题前面很简单，最后两道有点难
# 4-1到4-13都很简单，放到第一部分
# 4-14是要求阅读PEP 8,4-15锁紧，行宽，空行

# 4_1 定义一个函数，然后把函数打出来。
pizzas=['榴莲芝士披萨','海鲜至尊披萨','黑椒牛肉披萨']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(pizza+'超好吃')

print("我是真喜欢必胜客，尤其是白宇哥哥代言之后")

# 4_2 找三个有相同特点的生物，然后打印出来
creatures=['我','你','他']
for creature in creatures:
    print(creature)

for creature in creatures:
    print(creature+'爱吃披萨！')
    print('大家都爱吃披萨！')

# 4_3 数列1-20，并打印出来
for n in range(1,21):
    print(n)
#
# # 4_4 一个六位数，看一下多长时间能打印出来
# for n in range(1,1000001):
#     print(n)

# 4_5 求六位数中的最大值和最小值
a=range(1,1000001)
print(min(a))
print(max(a))
print(sum(a))

# 4_6 定义一个奇数列
for odd_number in range(1,20,2):
    print(odd_number)

# 4_7 3的倍数，步长为三
for multiple_of_three in range(3,31,3):
    print(multiple_of_three)

# 4_8 立方
b=[]
a=range(1,11)
for n in a:
    b.append(n**3)
print(b)

# 4_9 立方解析
cubic=[n**3 for n in range(1,11)]
print(cubic)

# 4_10 切片
a=range(1,11)
print("\nThe first three items in the list are:\n")
print(a[0:3])

for n in a[0:3]:
    print(n)

print("\nThe items from the middle of the list are:\n")
print(a[3:6])

for n in a[3:6]:
    print(n)

print(list(a[3:6]))

# 4_11 切片赋值
pizzas=['榴莲芝士披萨','海鲜至尊披萨','黑椒牛肉披萨']
pizzas_2=pizzas[:]

pizzas.append('巧克力奶茶披萨')
pizzas_2.append('土豆山药披萨')
print("\nMy favorite pizzas are:\n")
print(pizzas)
print("\nMy favorite pizzas are:\n")
print(pizzas_2)

# 4_12
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
#print(my_foods)
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
#print(friend_foods)
for food in friend_foods:
    print(food)

# 4_13 自助餐里面有什么
buffet=('烤肉','冰激凌','炸鸡','饮料','灌汤包')
for food in buffet:
    print(food)

buffet(0)='水果'
#can't assign to function call 无法分配给函数调用  元祖
#只能重新覆盖
buffet=('烤肉','水果','沙拉','饮料','灌汤包')
for food in buffet:
    print(food)

# 4_14 PEP8 https://www.python.org/dev/peps/pep-0008/解读
#作文格式规范指南
#PEP python Enhancement Proposal ----Python建议增强书
#怎么看？ 英文原文＋CSDN上的翻译
#--------目录
#--------介绍原则
#--------三个具体问题1.设置tab为四个空格  2.行长度80  3.空行

#introduction
#A Foolish Consistency is the Hobgoblin of Little Minds 人挪死树挪活
#Code Lay-out
#----indentation 缩进
#----tabs or spaces
#----maximum line length每行最大间距
#----should a line break before or after a binary operator？ 加号 before
#----blank lines 空行
#----source file encoding源文件编码
#----imports导入
#----module level dunder names模块级的呆名
#----string quotes字符串的引号
#----whitespace in expressions and statements 表达式和语句中的空格
#----pet peeves 不能忍受的事情
#----other recommendations 其它建议
#----comments注释
#----block comments 块注释
#----inline comments 行内注释
#----nameing conbentions 命名规范
#----overriding principlr 最重要的原则
#----descriptive naming styles 描述命名风格
#----prescriptive naming conventions 约定俗成命名约定
#----name to avoid 应该避免的名字
#----package and module names 包名和模块名字
#----class names 类名
#----exception names 异常名字
#----global variable names 全局变量名
#----function names 函数名
#----function and method arguments 函数和方法参数
#----method names and instance variables 方法名和实例变量
#----constants 常量
#----designing for inheritance继承的设计
#----public and internal interfaces 公共和内部的接口
#----programming recommendations 编程建议
#----function annotations功能注释

#PEP8 介绍 introduction

# 4_15 检查一下tab是四个空格
# File.settings.editor.code style.python
# File.settings.editor.general.appearance.whitespaces
# File.settings.editor.code style.right margin(columns)=80
