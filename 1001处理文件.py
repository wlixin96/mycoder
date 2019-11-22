# 10.1 从文件中提取数据

# 10.1.1 txt
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

### 结尾有个空行，用rstrip()去除

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    #### 我这个用完rstrip还是有空行

## 10.1.2 绝对路径
with open('D:\python10.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

## 10.1.3 逐行读取

filename='pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

filename='pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#
## 10.1.4 创建包含文件各行内容的列表readlines
filename='pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines)

## 10.1.5 使用文件的内容，列表又变字符串
filename='pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

## 10.1.6 pi后一百万位

filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[0:52])
print(len(pi_string))

## 10.1.7 圆周率中包含你的生日嘛
filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy:")

if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')

else:
    print('Your bt does not')

# 10.2 写入文件

## 10.2.1 写入空文件，如果文件不存在，会自动创建

filename = 'programing.txt'

with open(filename,'w') as file_object:
    file_object.write('当我们对视，我们眼里有对方，和色彩明丽的希望。')

## 10.2.2 换行

filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write('当我们对视')
    file_object.write('我们眼里有对方')
    file_object.write('和色彩明丽的希望。')

filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write('当我们对视\n')
    file_object.write('我们眼里有对方\n')
    file_object.write('和色彩明丽的希望\n')


## 10.2.3 附加到文件中

filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write('眼底热烈的感情日渐无法隐藏\n')
    file_object.write('再这样下去我们只会双双狠狠跌伤\n')
    file_object.write('还没有能力承担任何可能发生的后果\n')
    file_object.write('于是一个眼神肯定，这份爱已有意义\n')
    file_object.write('我们举杯互助前程似锦\n')
    file_object.write('决然转身，立于对立的两端\n')
    file_object.write('再次相遇，眼底是燃烧的余烬，汹涌的暗流\n')

# 10.3 异常 try except 抵御无意的错误与恶意的攻击

# 10.3.1 ZeroDivisionError

print(5/0)

# ## 10.3.2
#
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

## 10.3.3 创建一个执行除法运算的简单计算器

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")

    if first_number == 'q':
        break

    second_number = input("\nSecond number:")
    if second_number == 'q':
        break

    answer = int(first_number)/int(second_number)
    print(answer)


### 书上原话：P174，我仿佛得到了什么启示

# 10.3.4

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")

    if first_number == 'q':
        break

    second_number = input("\nSecond number:")
    if second_number == 'q': ##这里感觉书上少些一句 P174
        break

    try:
        answer = int(first_number)/int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero!")

    else:
        print(answer)

# 10.3.5 FileNotFoundError异常

filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read
# except FileExistsError:
except FileNotFoundError:
    msg="Sorry, the file "+filename+" does not exist."
    print(msg)

## 10.3.6 分析文本

## 先测一下split()的功能：以空格为分隔符将字符串拆分
title = 'shi jie da shen lun'
a = title.split()
print(a)

title = '世界大神论\n哈哈'
a = title.split()
print(a)
b=len(a)
print(b)

## 查文件

filename='programming.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg="\nSorry, the file "+filename+" does not exist."
    print(msg)

else:
    words = contents.split()
    num_words = len(words)
    print(words)
    print("The file "+ filename + " has about "+str(num_words)+" words.")

    ### txt read后面的括号没打都会报错
    ### 另外pycharm更新似乎很慢，文件改了，这边还没改

# 10.3.7 将这个功能做成一个函数

def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        msg = "\nSorry, the file " + filename + " does not exist."
        print(msg)

    else:
        words = contents.split()
        num_words = len(words)
        print("\n")
        print(words)
        print(
            "The file " + filename + " has about " + str(num_words) + " words.")

# filename='programming.txt'
# count_words(filename)
#

filenames=['alice.txt','programming.txt','a_discussion_of_the_great_mind_of_our_world.txt']
for filename in filenames:
    count_words(filename)
#
# 10.3.8 失败时一声不吭

def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        pass

    else:
        words = contents.split()
        num_words = len(words)
        print("\n")
        print(words)
        print(
            "The file " + filename + " has about " + str(num_words) + " words.")


filenames=['alice.txt','programming.txt','a_discussion_of_the_great_mind_of_our_world.txt']
for filename in filenames:
    count_words(filename)

# 10.4 存储数据
#
## 10.4.1

import json

numbers = [1,2,3,4,5,7,8]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
    n=json.load(f_obj)

print(n)

# 10.4.2 这个功能可以用来储存记录用户信息，比如记住我的名字和密码

import json

username = input("What is your name?")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, "+username+"!")

# 向储存了名字的用户发出问候

import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, "+username+"!")

## 两个程序合在一起

import json
# 如果以前存储了用户名就加载它
# 否则，就提示用户输入用户名并存储它

filename='username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj) ## 尝试打开文件
except FileNotFoundError:
    username = input("What is your name?") ##文件不存在，问你叫啥名
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)  ##输入的名字计入到目标文件中
        print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")

# 10.4.3 重构 每个功能，都单独拿出来做成一个函数

import json

def greet_user(): ## 定义成一个函数
    """问候用户，并指出其名字"""

    ### 上面的代码直接复制下来
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()

### 获取用户名，判断是否存储了用户名这部分分离出来

import json

def get_stored_username(filename):
    """如果存储了用户名，就获取它"""
    filename = filename ### 我把这里改成函数的变量了
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None ###这里用于下面做逻辑判断
    else:
        return username

def greet_user(filename):
    """问候用户，并指出其名字"""
    username=get_stored_username(filename)
    if username:
        print("Welcome back, "+username+"!")
    else:
        username=input("What is your name?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back, "+username+"!")

greet_user('username.json')
#
## 将else下面这部分提出来，当成一个单独的函数

import json

def get_stored_username(filename):
    """如果存储了用户名，就获取它"""
    filename = filename ### 我把这里改成函数的变量了
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None ###这里用于下面做逻辑判断
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    ### else下面的粘过来
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user(filename):
    """问候用户，并指出其名字"""
    username=get_stored_username(filename)
    if username:
        print("Welcome back, "+username+"!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+username+"!")

greet_user('user.json')

# # 10.5 小结，结什么，第十章基础完结，开心，下面就是做题啦！
In [ ]:
## 10.3.7 将这个功能做成一个函数

def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            # f_obj.flush()
    except FileNotFoundError:
        msg = "\nSorry, the file " + filename + " does not exist."
        print(msg)

    else:
        words = contents.split()
        num_words = len(words)
        print("\n")
        print(words)
        print(
            "The file " + filename + " has about " + str(num_words) + " words.")



filenames=['alice.txt','programming.txt','a_discussion_of_the_great_mind_of_our_world.txt']
for filename in filenames:
    count_words(filename)
In [ ]:
import json

numbers = [1,2,3,4,5,7,8]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
In [ ]:
# 习题 10-1 文件打开的三种方式

## 1
print("1 文件.read()方式:")
with open('cp_pepa_1.txt') as file_object:
    contents = file_object.read()
    print(contents)

## 2
print("2 for line in 文件 方式:")
filename='cp_pepa_2.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# 3
print("3 for line in 文件,加rstrip()处理:")
filename='cp_pepa_3.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

## 4
print("4 文件.readlines() 方式:")
filename='cp_pepa_4.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines)

# 10-2 replace() 字符串替换
#
msg="娘子 is real！"
print('\n'+msg)
msg=msg.replace('real','rio')
print('\n'+msg)


print("替换前")
with open('cp_pepa_5.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("替换后")
with open('cp_pepa_5.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('顾依凉','他')
    print(contents)

## 对中文的替换是好使的，啊啊啊因为我打错了顾一凉。。。
## 应为replace应该是以空格为单位在分割字符串，然后对比替换

print("替换前")
with open('cp_pepa_6.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("替换后")
with open('cp_pepa_6.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('Yiliang GU','He')
    print(contents)
#
# # ## 注意这个操作并没有改变文档本身
#
# # 10-3
#
filename = 'cp_pepa_7.txt'

with open(filename,'w') as file_object:
    msg=input("请输入:")
    file_object.write(msg)
# #
# # 你以为是新的大门向我敞开了吗？不，我探索见了一个全新的宇宙。我看见了一个美丽和谐欣欣向荣的正能量新世界。
#
# # 10-4 连续输入，一条占一行
#
filename = 'cp_pepa_8.txt'

with open(filename,'w') as file_object:
    while True:
        msg=input("请输入:")
        if msg != 'q':
            file_object.write(msg+'\n')
        else:
            break

# ##在这里，
# # 我对顾依凉微笑，是眼含春风。
# # 我跟顾依凉擦肩，是忍不回顾。
# # 我与顾依凉同框时低下了头，是不胜娇羞。
# # 我与顾依凉同框时转头与旁人说笑，是心仍相系。
#
# # 10-5 连续输入，一条占一行
#
# words=['在这里，',
       '顾依凉对我微笑，是欲语还休。',
       '顾依凉与我擦肩，是心中留恋。',
       '顾依凉与我同框时低下了头，是强忍喜爱。',
       '顾依凉与我同框时转头与旁人说笑，是假意避嫌。',
       ]

filename = 'cp_pepa_9.txt'

with open(filename,'w') as file_object:
    for word in words:
        file_object.write(word+'\n')
#
# 10-6 10-7 一起做了啊，想做一个计算器
#
print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")

    if first_number == 'q':
        break

    second_number = input("\nSecond number:")
    if second_number == 'q':
        break

    answer = int(first_number)+int(second_number)
    print(answer)

# # 10-6 10-7 excep ValueError 加法计算器

print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")

    if first_number == 'q':
        break

    second_number = input("\nSecond number:")
    if second_number == 'q':
        break

    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("不是数字你让我加什么加啊")
    else:
        print(answer)

# # 10-8 猫和狗 列表开文件，except 文件不存在
#
def read_txt(filenames):

    for filename in filenames:
        try:
            with open(filename) as file_object:
                contents = file_object.read()

        except FileNotFoundError:
            print('文件到底放哪了，整准了在让我找')

        else:
            print(contents)

filenames=['cp_pepa_10.txt',
           'cp_pepa_11.txt',
           'cp_pepa_102.txt']

read_txt(filenames)


# # 10-9 猫和狗 列表开文件，except pass
#
def read_txt(filenames):

    for filename in filenames:
        try:
            with open(filename) as file_object:
                contents = file_object.read()

        except FileNotFoundError:
            pass

        else:
            print(contents)

filenames=['cp_pepa_12.txt',
           'cp_pepa_13.txt',
           'cp_pepa_102.txt']

read_txt(filenames)

# # 10-10 count() 字符串中单词或短语出现了多少次
#
with open('cp_pepa_6.txt') as file_object:
    contents = file_object.read()
    print(contents)

print(contents.count('Yiliang GU'))
print(contents.count('yiliang gu'))
print(contents.lower().count('yiliang gu'))

# 10-11 10-12 json.dump 把书上的例子粘过来改

import json

def get_stored_number(filename):
    """如果存储了数字，就获取它"""
    filename = filename ### 我把这里改成函数的变量了
    try:
        with open(filename) as f_obj:
            number=json.load(f_obj)
    except FileNotFoundError:
        return None ###这里用于下面做逻辑判断
    else:
        return number


def get_new_number():
    """提示用户输入用户名"""
    ### else下面的粘过来
    number = input("What is your favorite number?")
    filename = 'number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number


def greet_user(filename):
    """问候用户，并指出其名字"""
    number=get_stored_number(filename)
    if number:
        print("I know your favorite number! It's "+number+"!")
    else:
        username=get_new_number()
        print("We'll remember that when you come back!")

greet_user('number.json')
# greet_user('.json') 可以再试一个不存在的文件

# # 10-13 没看懂