a=['alice','david','carolina']
for b in a:
    print(b)

for b in a:
    print(b.title()+', that was a great trick!')
    print("I can't wait to see your next trick, "+b.title()+".\n")

print("Thank you, everyone, That was a great magic show!")

#创建数字列表
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

#指定步长，只打印偶数
even_number=list(range(2,11,2))
print(even_number)

#前十个整数的平方
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#定义一组数，求其中最大值和最小值
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析，直接上
squares=[value**2 for value in range(1,11)]
print(squares)

#切片
print(squares[0:3])
print(squares[1:4])
print(squares[:4])
print(squares[2:])
print(squares[-3:])

#遍历，也就是循环列表中的一部分
players=['charles','martina','michaek','florence','eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#复制列表，其实就是切片并将值赋给新的列表，原列表不变
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

#直接a列表=b列表，ab相关联，a变b变，b变a变

a=[0,1,2,3]
b=a
a.append(4)
b.append(5)
print(a)

#元祖，不可改变的列表
dimensions=(200,500,1)
print(dimensions)
print(dimensions[1])
print(dimensions[0])

for dimension in dimensions:
    print(dimension)

dimensions=(10,20,30)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#PEP 8代码格式规范