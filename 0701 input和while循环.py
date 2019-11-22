# 7.1 input(x),意思是打印出x之后等待用户输入一个值

message=input("Tell me something, and I will repeat it back to you: ")
print(message)

# 7.1.1 打招呼
name=input("Please enter your name: ")
print("Hello, "+name+"!")

## 将这个事先需要打印的x先定义出来

prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nwhat is your first name?"### 注意这个+=，p=p+w

name=input(prompt)
print("\nHello, "+name+"!")


# 7.1.2 为了之后能够比较大小，输入的值要求是数字，整型int

age=input("How old are you?")
age=int(age)
print(age>=18)##测试一下这个数能不能作为数值用

height=input("How tall are you, in inches？")
height=int(height)

if height>=36:
    print('\nYou are tall enough to ride!')
else:
    print("\nYou'll be able to ride when you're a litter older.")

# 7.1.3求余数
print(4%3)
print(5%3)

# 奇数偶数判断
number=input("Enter a number, and I'll tell you if it's even or odd:")
number=int(number)

if number % 2==0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")


# 7.2.1 while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

# 7.2.2quit就退出
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=''
while message != 'quit':
    message=input(prompt)
    if message!='quit':
        print(message)

## 用False，Ture来决定是否退出
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."

active=True
while active:
    message=input(prompt)

    if message=='quit':
        active=False
    else:
        print(message)

# 用break退出
prompt="\nPlease enter the name of a city you have visitied:"
prompt+="\n(Enter 'quit' when you are finished.)"

while True:
    city=input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")


#continue 忽略之后的代码
current_number=0
while current_number<10:
    current_number+=1
    if current_number % 2 ==0:
        continue
    print(current_number)

# 7.3.1 从一个列表，转移到另一列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 7.3.2 删除列表中的所有某个元素

pets=['a','b','c','d','c','c']
print(pets)

while 'c' in pets:
    pets.remove('c')

print(pets)


#7.3.3 用户输入字典
responses={}
polling_active=True

while polling_active:
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")

    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False

print("\n---Poll Results---")
for name, response in responses.items():
    print(name+' would like to climb '+response+".")
In [ ]:
# 习题7-1

vehicle=input("What kind of vehicle would you like to try?")

print('Ok, I will show you the series of '
      +vehicle
      +', this way plese.')

# 习题7-2 输入数字，加入判断
number=input("Vous avez combien de personne?")
number=int(number)
if number>=8:
    print("Je suis desole, il n'y a pas assez de place.")
else:
    print("Par ici, s'il vous plait.")

## 习题7-3 10的整数倍
question='Tell me a number.'
question+='\nThen I will show you if it is multiple of ten.'
number=input(question)

number=int(number)  ##这个转换必须有！！！

if number % 10 == 0:
    print('Yes,it is!')
else:
    print('No, it is not.')

# 7-4

print('输入你想要的配料，输入quit退出')
topping=''
while topping != 'quit': #用中文输入法输入符号，会有红色下划线
    topping=input("What would you like to add on you pizza?")
    if topping != 'quit':
        print('add some '+topping)

# 7-5 while询问年龄 见7-6



# 7-6 三个出口

## 1while条件测试结束循环

## 判断退出，''定义一个空变量，
## 当负负得正的时候，实行while，input，
## 如果不等于quit打印，打印，继续循环
## 等于quit不打印，循环结束

print('输入年龄，得到票价，*号退出')
age=''

while age!='*':
    age=input('How old are you？')
    if age != '*':
        age=int(age)
        if age<0:
            print('别闹，重新输入')
            continue
        elif age>=0 and age<3:
            price=0
        elif age>=3 and age<=12:
            price=10
        elif age>12:
            price=15
        print('You admission cost is '+price.__str__()+'$.')

print('输入年龄，得到票价，*号退出')

## 2active测试循环

active = True

while active:
    age=input('How old are you？')
    if age != '*':
        age=int(age)
        if age<0:
            print('别闹，重新输入')
            continue
        elif age>=0 and age<3:
            price=0
        elif age>=3 and age<=12:
            price=10
        elif age>12:
            price=15
        print('You admission cost is '+price.__str__()+'$.')
        ## 这里必须有.str
    else:
        active = False

## break


while True:  ### 这里直接用True
    age=input('How old are you？')
    if age != '*':
        age=int(age)
        if age<0:
            print('别闹，重新输入')
            continue
        elif age>=0 and age<3:
            price=0
        elif age>=3 and age<=12:
            price=10
        elif age>12:
            price=15
        print('You admission cost is '+price.__str__()+'$.')
        ## 这里必须有.str
    else:
        break

# 7-7 无线循环
# n=1
# while True:
#     print(n)
#     n+=1

# 7-8 熟食店

sandwich_orders=['蛋黄三明治','奶酪火腿三明治','三文鱼三明治']
finished_sandwiches=[]

while sandwich_orders:
    sandwich=sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print('finished sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich)

# 习题 7-9 五香牛肉

sandwich_orders=['五香牛肉','蛋黄','奶酪','三文鱼','五香牛肉','五香牛肉']

while '五香牛肉' in sandwich_orders:
    sandwich_orders.remove('五香牛肉')

for sandwich in sandwich_orders:
    print(sandwich)

# 习题 7-10

name_places={}

print('问卷调查，任何时候，打"你奏凯"退出')

while True:
    name=input("您的名字")
    if name == '你奏凯':
        break
    else:
        place=input("您最想去的地方？")
        if place=='你奏凯':
            break
        else:
            name_places[name]=place

print('调查结束，结果为：')

for name, place in name_places.items():
    print(name+'最想去的地方:'+place+'。')