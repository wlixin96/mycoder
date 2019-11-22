#列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
#------------------ctrl+/  加注释

#使用列表中的各个值
message='my first bicycle was a '+bicycles[0].title()+'.'
print(message)

#修改列表元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

#添加列表元素
motorcycles.append('ducati') #在末尾处添加
print(motorcycles)
motorcycles.insert(0,'ducati') #在0位添加
print(motorcycles)

#先创建空列表，后向里面添加元素
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 列表删除元素
del motorcycles[0]
print(motorcycles)

#pop函数，弹出列表最后的元素
motorcycles=['a','b','c']
print(motorcycles)
#所以一般执行这个函数的时候就要赋值，才能将踢出的元素保存

motorcycles.pop()
print(motorcycles)

poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

motorcycles=['honda','ymaha','suzuki']
last_owned=motorcycles.pop()
print('The last motorcycle I owned was a '+last_owned.title()+'.')

#弹出列表中任意位置的元素
first_owned=motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')

#根据值删除元素
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#remove 删除
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive')

#对列表元素首字母进行永久性排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#对列表元素首字母进行永久性反序
cars.sort(reverse=True)
print(cars)

#临时排序，调用函数：y=f(x),本身的x没有变；x，f()相当于x=f(x).x
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)
