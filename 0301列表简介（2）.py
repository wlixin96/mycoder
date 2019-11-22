# 3_1 姓名列表，访问元素，打印出来
onepiece=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji','Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']
print(onepiece[0])
print(onepiece[1])
print(onepiece[2])
print(onepiece[3])
print(onepiece[4])
print(onepiece[-6])
print(onepiece[-5])
print(onepiece[-4])
print(onepiece[-3])
print(onepiece[-2])
print(onepiece[-1])

# 3_2 姓名列表，打印人名+问候语
print('Love you '+onepiece[0])
print('Love you '+onepiece[1])
print('Love you '+onepiece[2])
print('Love you '+onepiece[3])
print('Love you '+onepiece[4])
print('Love you '+onepiece[-6])
print('Love you '+onepiece[-5])
print('Love you '+onepiece[-4])
print('Love you '+onepiece[-3])
print('Love you '+onepiece[-2])
print('Love you '+onepiece[-1])

# 3_3 通勤方式列表，打印一些列有关通勤方式的宣言
transport=['大妈','路飞','leijiu']
print(transport[0]+'是我的最最理想型')

3_4 邀请晚宴名单，发出邀请
guests=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji','Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']
print("Welcome to the wedding, "+guests[0])
print("Welcome to the wedding, "+guests[1])
print("Welcome to the wedding, "+guests[2])
print("Welcome to the wedding, "+guests[3])
print("Welcome to the wedding, "+guests[4])
print("Welcome to the wedding, "+guests[5])
print("Welcome to the wedding, "+guests[6])
print("Welcome to the wedding, "+guests[7])
print("Welcome to the wedding, "+guests[8])
print("Welcome to the wedding, "+guests[9])
print("Welcome to the wedding, "+guests[10])

# 3_5 修改嘉宾名单
a=guests[1]
guests.remove(a)
print(a+' cannot come.')
guests.append('老鹰记者')
print("Welcome to the wedding, "+guests[0])
print("Welcome to the wedding, "+guests[1])
print("Welcome to the wedding, "+guests[2])
print("Welcome to the wedding, "+guests[3])
print("Welcome to the wedding, "+guests[4])
print("Welcome to the wedding, "+guests[5])
print("Welcome to the wedding, "+guests[6])
print("Welcome to the wedding, "+guests[7])
print("Welcome to the wedding, "+guests[8])
print("Welcome to the wedding, "+guests[9])
print("Welcome to the wedding, "+guests[10])

# 3_6
guests.insert(0,'German')
guests.insert(4,'Fire Tank')
guests.append('Big Mom')
print("Welcome to the wedding, "+guests[0])
print("Welcome to the wedding, "+guests[1])
print("Welcome to the wedding, "+guests[2])
print("Welcome to the wedding, "+guests[3])
print("Welcome to the wedding, "+guests[4])
print("Welcome to the wedding, "+guests[5])
print("Welcome to the wedding, "+guests[6])
print("Welcome to the wedding, "+guests[7])
print("Welcome to the wedding, "+guests[8])
print("Welcome to the wedding, "+guests[9])
print("Welcome to the wedding, "+guests[10])
print("Welcome to the wedding, "+guests[11])
print("Welcome to the wedding, "+guests[12])
print("Welcome to the wedding, "+guests[13])

# 3_7
print('\nSorry, there are only two places left')
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
a=guests.pop(-1)
print('The wedding is canceled, franchement desole,'+a)
print(guests)
#对剩下的两位，打印一句话
print('\n有缘千里来相会，雷玖在等你'+guests[1])
print('我从远方赶来赴你一面之约'+guests[0])
#删除余下两位
del guests[0]
del guests[0]
print(guests)

3_8 放眼世界，想出至少5个你想去的地方，顺序打乱
to_the_place_I_belong=['Swizerland','my side','higher dimentional space','my home','argentina']

#打印原始列表
print("The original list:\n")
print(to_the_place_I_belong)
#
#sorted()按字母顺序打印，不改变原来列表的顺序
print("\nSorted list:\n")
print(sorted(to_the_place_I_belong))

#再次打印确认列表顺序没有变
print("\nThe original list again:\n")
print(to_the_place_I_belong)

#sorted()反序，不改变列表原来顺序，reverse=True
print("The list after being sorted_reverse=True:\n")
print(sorted(to_the_place_I_belong,reverse=True))

#再次打印确认列表顺序没有变
print("\nThe original list again:\n")
print(to_the_place_I_belong)

#reverse() 反转
to_the_place_I_belong.reverse()
print("\n用reverse反转列表的效果\n")
print(to_the_place_I_belong)

#reverse ()再次反转
to_the_place_I_belong.reverse()
print("\n用reverse再次反转列表的效果\n")
print(to_the_place_I_belong)

#用sort()改变列表本身的顺序
print('\nThe list after being ordered by sort()\n')
to_the_place_I_belong.sort()
print(to_the_place_I_belong)

#用sort()反序
print('\nThe list after being ordered by sort(reverse=True)\n')
to_the_place_I_belong.sort(reverse=True)
print(to_the_place_I_belong)

# 3_9 哎呀，早点说呀，我怎么吧len()这个函数忘了
onepiece=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji','Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']
print(len(onepiece))

# 3_10 自建列表，尝试使用本章的所有函数

# 1.访问
# 2.修改
# 索引只怼
print(onepiece)
onepiece[0]='Charlotte Linlin'
print(onepiece)
# 3.添加
onepiece.append('Chalotte Linlin') #末尾添加
onepiece.insert(0,'Shanks0')#根据索引插入
print(onepiece)
# 4.删除
del onepiece[2]#根据索引删除，特点是删了就删了，这个值不能给别人
print(onepiece)

a=onepiece.pop(2)
#默认弹出最后一个，特点从列表中弹出，可以给别人
#需要知道索引位置
print(a)
print(onepiece)

a=onepiece.remove('Monkey·D·Luffy')
print(onepiece)
print(a)

#特点，不知道索引位置，知道元素是什么
#remove出去的元素不可以通过赋值继续
#特点，不知道索引位置，知道元素是什么
#remove出去的元素不可以通过赋值继续使用
#剩下就是对列表一顿操作的函数，各种排序，上一道题做过了，不想搞了

#3_11 有意引发错误

list=['a','b','c']
list[3]
a=list.remove('d')







