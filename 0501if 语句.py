cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#==的含义，条件测试，检查是否等于，而不是赋值

car='bmw'
a=car=='bmw'
print(a)
b=car=='audi'
print(b)
c=car=='Bmw'#区分大小写
print(c)

#当不想区分大小写时，都转换为小写
car='Audi'
d=car.lower()=='audi'
print(d)
print(car)#原来的car没有被改变

#if不等于
requested_topping='mushroom'
if requested_topping !='cnchovies':
    print("Hold the anchovies")

#对数字的判断
age=18
g=age==18
print(g)

answer=17
if answer!=42:
    print("That is not correct answer,please tre again!")

#对数字判断的特有符号
age=18
h=age==18
i=age<19
j=age>21
k=age>=18
l=age<=19
print(h,i,j,k,l)

#且，或
age_0=22
age_1=18

print(age_0>21 and age_1>=21)
print(age_0>21 or age_1>=21)

#是否存在于列表
a=[1,2,3,4,5]
print(1 in a)
print(2 in a)
#是否不再
a=[2,3,4,5,6]
if 1 not in a:
    print("No, I cannot find this")

#if语句，else，投票的例子
age=19
if age>=18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print("Sorrt,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#门票的判断
age=12
if age<=4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#简化版，price提出来
print("\n简化版")
age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10

print("Your admission cost is $"+str(price)+".")

#省略else
print("\n都用elif,不用else的情况：")
age=60
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5
print("Your admission cost is $"+str(price)+".")

#检查元素
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+'.')
print('\nFinished making your pizza!')

#for+if，没有青椒了
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:\
        print("Adding"+requested_topping+'.')
print('\nFinished making your pizza!')

#没点额外配料，列表为空时，判断默认值为false
requested_toppings=[]
if requested_toppings:#列表不是空的时候
    for requested_topping in requested_toppings:
        if requested_topping =="green oeooers":
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding "+ requested_topping +'.')
    print('\nFinished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")

#多个列表
availabale_toppings=['mushrooms','olives','green peppers','pepper']
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabale_toppings:
        print("Adding"+requested_topping)
    else:
        print('Sorry we donnot have '+requested_topping+'.')
print("\nFinished make your pizza!")

# 5_1 条件测试：预期＋答案
wo='hao kan'
print("Is wo == 'hao kan'? I predict True.")
print(wo =='hao kan')
print("\nIs wo == 'yi ban hao kan'? I predict False.")
print(wo == 'yi ban hao kan')

# 5_2 更多条件测试，每个都来一个True，来一个False

#字符串
string_1='Big mama'
string_2='Big mama'
string_3='Big Mama'

print('\nstring_1==string_2:')
print(string_1==string_2)

print('\nstring_1==string_3:')
print(string_1==string_3)

#使用lower()的测试
print('\nstring_1.lower()==string_3.lower():')
print(string_1.lower()==string_3.lower())

#检查两个数字
age_julaosh=31
age_beilaoshi=29

print('\nage_julaoshi==age_beilaoshi:')
print(age_julaosh==age_beilaoshi)

print('\nage_julaoshi!=age_beilaoshi:')
print(age_julaosh!=age_beilaoshi)

print('\nage_julaoshi>=age_beilaoshi:')
print(age_julaosh>=age_beilaoshi)

print('\nage_julaoshi<=age_beilaoshi:')
print(age_julaosh<=age_beilaoshi)

#and or
print('\nFalse and True:')
print(age_beilaoshi==age_julaosh and age_julaosh!=age_beilaoshi)

print('\nFalse and True:')
print(age_beilaoshi==age_julaosh or age_julaosh!=age_beilaoshi)

# 测试特定的值是否包含在列表中
zyL48=['weiwei','mianmian','xiaoxue','shengge','kaixin']
#不允许使用小写的L，命名规则，在有些编译器中小写的L与数字1分不清楚

print("\nIs 'mianmian' in zyL48?")
print('mianmian' in zyL48)

print("\nIs 'maohou' in zyL48?")
print('maohou' in zyL48)

print("\nIs 'maohou' not in zyL48?")
print('maohou' not in zyL48)

# 5_3 外星人颜色if

print('\n三体监听员：不要回答不要回答')

yewenjie='没回答'
if yewenjie == '没回答':
    print('叶文洁没有回答，于是')
    print('全剧终')

print('\n三体监听员：不要回答不要回答')

yewenjie='回答'
if yewenjie == '没回答':
    print('叶文洁没有回答，于是')
    print('全剧终')

yewenjie='回答'
if yewenjie == '回答':
    print('叶文洁没有回答，于是')

#if else
##测试通过
print('\n叶文洁：如果思想可以直接显示在头顶，三体人的头有颜色吗？')
print('三体人，各种颜色都有')
print('叶文洁：你是什么颜色？')
trisolaran_color='yellow'

if trisolaran_color=='green':
    print('三体监听员：绿色。')
    print('叶文洁：你这个颜色在我们地球很不吉利啊。')
    print('三体监听员：。。。')
else:
    print('三体监听员：平时没有颜色，近乎半透明，只有思考的时候会显示出黄色。')
    print('叶文洁：你这个思想在我们地球估计不能过审啊。')
    print('三体监听员：。。。')

# 5_5 外星人颜色，无聊，我改成了路飞打怪升级的例子。
#     路飞打败相应的敌人，悬赏金就有相应的提升

boss='?'
if boss=='恶霸-阿龙':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('| B 30 000 000 |')
    print('|     ---Marine|')

elif boss=='七武海-老沙':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('|B 100 000 000 |')
    print('|     ---Marine|')

elif boss=='CP9-路奇':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('|B 300 000 000 |')
    print('|     ---Marine|')

elif boss=='大事件-救艾斯':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('|B 400 000 000 |')
    print('|     ---Marine|')

elif boss=='七武海-多弗朗明哥':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('|B 500 000 000 |')
    print('|     ---Marine|')

elif boss=='七武海-多弗朗明哥':
    print('| ~~ WANTED ~~ |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|              |')
    print('|DIED OR  ALIVE|')
    print('|MONKEY D LUFFY|')
    print('|B 500 000 000 |')
    print('|     ---Marine|')

# 习题5-6 人生的不同阶段
age_naruto=60

if age_naruto==0:
    print('\nNaruto刚出生时，正值九尾之战，水门夫妇牺牲，九尾被封印在Naruto体内')
if age_naruto>0 and age_naruto<12:
    print('\n幼年Naruto在孤独中成长，到处捣乱以引起注意')
if age_naruto>=12 and age_naruto<13:
    print('\nNaruto成为下忍')
if age_naruto>=13 and age_naruto<17:
    print('\nNaruto晋升中忍')
if age_naruto>=17 and age_naruto<23:
    print('\nNaruto晋升上忍')
if age_naruto>=23 and age_naruto<30:
    print('\nNaruto成为火影，结婚生娃')
if age_naruto>=30 and age_naruto<65:
    print('\nNaruto继续当火影，工作养家')
if age_naruto>=65:
    print('\nNaruto退休养老，不过也有可能像三代一样，干到满脸褶')

# 习题5-7 喜欢的水果
favorite_fruits=['durian','small durian','big durian','huge durian']

if 'small durian' in favorite_fruits:
    print('您真有品味！！')

if 'banana' in favorite_fruits:
    print('您真有品味！！')


if 'apple' in favorite_fruits:
    print('您真有品味！！')

if 'huge durian' in favorite_fruits:
    print('惊为天人，求你跟我做朋友')


# 习题 5-8，特殊对待
names=['卢梭 Rousseau','弗洛伊德 Freud','海德格尔 Heidegger','叔本华 Schopenhauer','马克思 Marx']

for name in names:
    print(name+' 你说的挺好')
    if name == '马克思 Marx':
        print('666 666')

#习题 5-9

names=[]
if not names:
    for name in names:
        print(name+' 你说的挺好')
        if name == '马克思 Marx':
            print('666 666')
else:
    print('We need to find some users！')

# 习题5-10 检查用户名
current_users=['Rousseau','Freud','Heidegger','Schopenhauer','Marx']
new_users=['ROUSSEAU','Freud','Thoreau','Leibniz','Dostoevsky']
current_users_lower=[]

# 转换为小写原始名单全部
for current_user in current_users:
    name_lower=current_user.lower()
    current_users_lower.append(name_lower)

# 检查新旧名单是否重复，统一成小写
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user+',请不要重复报名！')
    else:
        print(new_user+',恭喜注册成功！')

# 习题5-11 1-9

numbers=range(1,10)
for number in numbers:
    if number==1:
        print(number+'st')
    elif number==2:
        print(number.__str__()+'nd')
    elif number==3:
        print(number.__str__()+'rd')
    else:
        print(number.__str__()+'th')

# 习题 5-12 检查 正确 不说了，不正确也运行不出来啊
# 习题 5-13 我又膨胀了，让我设想

