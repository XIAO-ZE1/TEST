# format
a=2.3
b=3.1415926
print('%4.2f+%4.5f'%(a,b),end=' ')
print(f'{a}+{b}',type(a))

# input
# name=input('你是谁\n')
# print('你好'+name) 

# if
age=10
if age>=18:
    print('我已成年')
elif age<8:
    print('我未成年')
else:
    print('我是青少年')

# while 猜数字
# import random
# num=random.randint(1,100)
# count=0
# while True:
#     guess=int(input('请输入一个数字：'))
#     count+=1
#     if guess==num:
#         print('恭喜你猜对了')
#         break
#     elif guess>num:
#         print('猜大了')
#     else:
#         print('猜小了')
# print(f'你一共猜了{count}次')

# for 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}\t',end=' ')
    print()
# # for 斐波那契数列
# n=int(input('请输入一个正整数：'))
# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     a,b=b,a+b

# 函数 
# 定义一个函数add，接收两个参数a和b
def add(a,b):
    # 返回a和b的和
    return a+b
print(add(1,2),type(add))
print()

#list 
print('list')
a=[1,2,3,4,5]
# 打印列表a的第一个元素、最后一个元素、第二个到第三个元素、除了最后一个元素之外的所有元素、列表a的逆序
print(a[0],a[-1],a[3:1:-1],a[:-1],a[::-1])
a.append(6)
print(a)
a.insert(0,0)
print(a)
a.remove(3)
print(a)
a.pop()
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print(len(a))
print(sorted(a))
a.clear()
print(a)
print()

# tuple 不可修改的列表
print('tuple')
t1=(1,2,2,4,5)
t2=(1)
t3=(1,)# 元组只有一个元素时，需要加逗号
print(type(t2),type(t3))
print(t1.index(2),t1.count(2),len(t1))
print()

# string
print('string')
str='hello world'
print(str[0],str[-1],str[1:3],str[:-1],str[::-1])
print(str.upper(),str.lower(),str.capitalize(),str.title(),str.replace('hello','hi'),str.split(),str.index('world'),str.count('l'),str.split('l'),str)
print()

# set 无序不重复的集合
print('set')
a={1,2,3,4,5}
a.add(6) # 添加元素
print(a)
a.remove(3) # 删除指定元素
print(a)
a.pop() # 随机删除一个元素
print(a)
print(a.difference({2,4,5}))# 求差集
print(a.intersection({2,4,5})) # 求交集 
print(a.union({7,8,9}))# 求并集
a.clear() # 清空集合
print(a)
print()

# dict 无序不重复的键值对集合
print('dict')
a={'name':'张三','age':18,'sex':'男'}
for i in a:
    print(i,a[i])
print(a['name'],a['age'],a['sex'])
print(a.keys(),a.values())
a['name']='李四'
print(a)
a.pop('age')
print(a)
a.clear()
print(a)
print()
# dict的key必须是不可变类型，如int、str、tuple等，value可以是任意类型

# 匿名函数
def func(add):
    result=add(1,2)
    print(result)
func(lambda x,y:x+y)
print()

# 文件
f=open('test.txt','w')
f.write('hello world')
f.close()
f=open('test.txt','a')
f.write('\nhello world')
f.close()

f=open('test.txt','r')
print(f.readlines())
f.close()
f=open('test.txt','r')
print(f.read())
f.close()
with open('test.txt','r') as f:
    for line in f:
        line=line.strip() # 去除换行符
        print(line.split(),end=' ')
print('\n')

# 异常处理
try:
    f=open('test1.txt','r')
    print(f.read())
except FileNotFoundError as e:
    print('文件不存在',e)
finally:
    f.close()
print()

# 模块
import time # 操作系统模块
from os import path
print(path.exists('test.txt'))
print(path.getsize('test.txt'))
time.sleep(.1)
print(time.ctime()) # 获取当前时间
# 自定义模块
import my_utils.str_util as str
import my_utils.file_util as file
print(str.substr('hello',1,3))
file.print_file_info('test.txt')
print()
# import winsound
# winsound.Beep(8500,1500) 
# pip 安装第三方模块 镜像: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 模块名
# import numpy 


# json
import json
data=[{"name":"张三","age":18,"gender":"男"},{"name":"李四","age":19,"gender":"女"},{"name":"王五","age":20,"gender":"男"}]
wt=json.dumps(data,ensure_ascii=False,indent=4)
with open('data.json','w',encoding='utf-8') as f:
    f.write(wt)
rd=json.load(open('data.json','r',encoding='utf-8'))
for i in rd:
    print(i['name'],i['age'],i['gender'])
print()

# class 面向对象：封装，继承，多态
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f'Employee name: {self.name}, age: {self.age}')

class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age) # call parent class
        self.salary = salary
    def __say(self): # private method
        print('I am a full time employee')
    def print_info(self):
        super().print_info()
        print(f'Salary: {self.salary}')
        self.__say()
    def __str__(self): # magic method
        return f'FullTimeEmployee: {self.name}, {self.age}, {self.salary}'

class PartTimeEmployee(Employee):
    def __init__(self, name, age, hours):
        super().__init__(name, age)
        self.hours = hours
    def print_info(self):
        super().print_info()
        print(f'Hours: {self.hours}')
    def __str__(self): # magic method
        return f'PartTimeEmployee: {self.name}, {self.age}, {self.hours}'

def info(employee:Employee):
    employee.print_info()

a=FullTimeEmployee('John', 30, 50000)
b=PartTimeEmployee('Tom', 25, 10)

if __name__ == '__main__':
    a.print_info() # 继承
    print(a) # __str__
    info(a) # 多态
print()


# 注解
def add(x:int,y:int)->int:
    return x+y
add(1,2)
from typing import Union
my_list: list[Union[int,float]] = [1,2,3.14]