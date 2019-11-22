# 字典 大括号
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# 访问字典中的元素 中括号
alien_0={'color':'green','points':5}
new_points=alien_0['points']
print("You just earned "+str(new_points)+" points!")

# 添加字典中的元素 中括号 快捷键ctrl+z

alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

# 改变子弹中的元素 中括号

alien_0={'color':'green','points':5}

print("The alien is "+alien_0['color']+'.')##当前颜色
alien_0['color']='yellow'#改变颜色为黄色
print("The alien is now "+alien_0['color']+'.')

# 对字典中的元素值做出判断

alien_0={'x_position':0,"y_position":25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))

#删除
alien_0={'color':'green','points':5}
del alien_0['points']
print(alien_0)

#字典的其他格式，注意换行的位置，最后多加了一个逗号
favorite_langues={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print(favorite_langues)

#遍历字典 把前面这个单词，含义分别打出来
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key, value in user_0.items():
    print("\nkey: "+key)
    print("Value: "+value)

# 生词 解释分开用
favorite_langues={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name, language in favorite_langues.items():
    print(name.title()+"'s favorite language is "+language.title()+'.')

for name in favorite_langues.keys():
    print(name.title())

# 对于字典中的人，打出名字，如果这个人在friends里面，多打出一句话
favorite_langues={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends=['phil','sarah']

for name in favorite_langues.keys():
    print(name.title())

    if name in friends:
        print("Hi, "+name.title()+", I see your favorite language is "+favorite_langues[name].title()+"!")

# 如果这个人不在喜欢语言这个名单中，说明他没参加采访，告诉他请投票
favorite_langues = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_langues.keys():
    print("Erin, please take our poll!")

# 按顺序，字典中的东西没有顺序，我们如果想按一定的顺序打，需要用sorted
favorite_langues = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 按字母顺序打印出来这个人名
for name in sorted(favorite_langues.keys()):
        print(name.title()+", thank you for taking the poll")

print("The following languages have been metioned:")

# 按原来字典中的顺序打印出语言，这里会重复打印
for language in favorite_langues.values():
    print(language.title())

# 不重复打印，用set

favorite_langues = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been metioned:")
for language in set(favorite_langues.values()):
    print(language.title())

#嵌套  列表=['字典0','字典1','字典2']

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# 生成30个外星人

aliens=[]   ##创建一个空列表
for alien_number in range(30): ##从0到29取值30次
    new_alien={'color':'green','points':5,'speed':'slow'}
    ##但这个外形人的编号在循环并没有使用
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)##打印出前5个
print('……')##后面的省略
##打印出外星人的数量，用len，注意转换为str
print("Total numeber of aliens: "+str(len(aliens)))

##前三个改成颜色速度分数值
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
##打印出前五个
for alien in aliens[:5]:
    print(alien)
print('……')

## 前五个外星人升级
for alien in aliens[0:5]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

for alien in aliens[:5]:
    print(alien)
print('……')


# 字典={'单词1':'解释1','单词2':['解释1','解释2']}

pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print('You ordered a '+pizza['crust']+'-crust pizza'+" with the following toppings:\n")

## 这里点名pizza字典里的crust这个词儿，把他的内容取出来过来

for topping in pizza['toppings']:##这里吧toppings的值取出来
    print('\t-'+topping)


# 字典中的多个列表

favorite_langues={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

## 元素分开name取成值，languages取成列表

for name,languages in favorite_langues.items():
    print('\n'+name.title()+"'s favorite languages are:")
    ##从列表再提出元素
    for language in languages:
        print("\t"+language.title())

# 字典中的字典 字典={字典0，字典1}
# 字典={'新华字典':{'我':'美丽'}，'牛津字典':{'Me':'beau'}，'Le petit Nicola':{'Moi':'La plus belle'}}
users={
    'aeinstein':{
        'first':'albert',
        'last':'ainstein',
        'location':'princeton',
    },
    'marie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
}
}

for username, user_info in users.items():

    print("\nUsername: "+username)

    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']

    print('\tFull name: '+full_name.title())
    print('\tLocation: '+location.title())
# 习题6-1 使用一个字典 存信息打出来

durian_mille_crepe_cake={'durian':'炒了',
                         'mille crepe':'煎了',
                         'cake':'抹上',
                         }

print(durian_mille_crepe_cake)

# 习题6-2

favorite_number={'a':1,'b':2,'c':3,'d':4,'e':5}
print(favorite_number)

# 习题6-3

python_words={'Code lay out':'代码布局',
              'Whitespaces in Expressions':'表达式中的空格',
              'Comments':'注释',
              'Naming Conventions':'命名规范',
              'programming recommendations':'编程建议'}

# .items()不要忘，为了调用字典中的值

for word, explaination in python_words.items():
    print("\n"+word+":")
    print(explaination)

# 6-3 python专业词汇字典

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

# 习题6-4
for word, explaination in python_words.items():
    print("\n"+word+":")
    print(explaination)

# 6-5 河流 国家

rivers={'La Seine':'France','yellow river':'China','Nile':'Egypt'}

for river, country in rivers.items():
    print("\nThe "+river.title()+" runs through "+country+'!!')

for river, country in rivers.items():
    print(river)

for river, country in rivers.items():
    print(country)

# 6-6 名单列表，字典，在列表中不在列表中区别打印

king_seven_armed_sea=['鹰眼','老沙','九蛇','明哥','甚平','月光莫利亚','熊','罗','巴基']
the_defeated={'老沙':'歇菜','月光莫利亚':'完蛋','熊':'打不过跑','甚平':'收编'}

for name in king_seven_armed_sea:
    if name in the_defeated.keys():
            print(name+'，嘿兄弟老熟人了啊')
    else:
        print(name,'，你等着')

# 6-7 三个字典合成一个字典

durian_mille_crepe_cake={'durian':'炒了',
                         'mille crepe':'煎了',
                         'cake':'抹上',
                         }

tomato_egg={'tomato':'切了',
            'egg':'炒了',
            'suger':'适量',
            'salt':'适量'}

palace_exploded_chicken_man={'peanut':'爆炒',
                             'chicken':'腌好',
                             'carrot':'切丁'}

cook_books=[durian_mille_crepe_cake,
            tomato_egg,
            palace_exploded_chicken_man,
            ]

for dish in cook_books:
    for ingredient, method in dish.items():
        print("\n材料："+ingredient+"：")
        print("方法："+method)

# 6-8 宠物

tom={'type':'cat','host':'一个只有脚出境的女的'}
jerry={'type':'耗子','host':'观众'}
speike={'type':'dog','host':'一个只有脚出境的女的'}

pets=[tom,jerry,speike]

for pet in pets:
    for key, value in pet.items():
        print('\n'+key+":"+value)

# 6-9 喜欢的地方，字典套列表{'':[]}

favorite_places={'依萍':['大上海','可云家','火车站'],
                 '如萍':['书桓家','公园','上海大桥'],
                 '陆飞':['如萍学校','报社','战场'],
                 }

for name, places in favorite_places.items():
    print("\n"+name+'喜欢的地方：')
    for place in places:
        print(place)

# 6-10 喜欢的数字
favorite_number={'a':[1,2,3],
                 'b':[4,5,6],
                 'c':[7,8,9],
                 'd':[10,11,12],
                 'e':[13,14],
                 }
for name, numbers in favorite_number.items():
    print("\n"+name+"喜欢的数字是：")
    for number in numbers:
        print(number)

# 6-11 城市 字典套字典a={'a':{}}

# bordeux={'country':'france',
#          'population':243636,
#          'fact':'水镜广场比特沙丘',
#          }
#
# larochelle={'country':'france',
#          'population':100000,
#          'fact':'港口水族馆海贼梦世界尽头的灯塔',
#          }
#
# barcelona={'country':'spain',
#          'population':1610000,
#          'fact':'建筑教堂佛朗明哥圆圈舞水果海鲜管够',
#          }

# places={bordeux,larochelle,barcelona}

places={'bordeux':{
         'country':'france',
         'population':'243636',
         'fact':'水镜广场比特沙丘',
         },
        'larochelle':{
        'country':'france',
         'population':'100000',
         'fact':'港口水族馆海贼梦世界尽头的灯塔',
         },
        'barcelona':{'country':'spain',
         'population':'1610000',
         'fact':'建筑教堂佛朗明哥圆圈舞水果海鲜管够',
         },
        }

for city, info in places.items():
    print("\n\n"+city+'介绍:')
    for key, value in info.items():
        print('\n'+key+':'+value)




# 6-12 扩展，差不多行了哈，你以为我真的会去做吗，果断略过