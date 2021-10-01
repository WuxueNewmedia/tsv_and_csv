#!/usr/bin/env python
# coding: utf-8

# # week04数据库中的用户信息
# * 知识点_用户输入
# * beerwall
# * 课程表优化2

# In[1]:


# 数据库中的用户信息
user_data = "李许娣"
password_data = "lxd123"
count = 3
while True:
    # count 自减去1
    count -= 1
    if count == -1:
        print("错了三次了，笑死了，请五分钟之后再尝试")
    # 用户登录输入的信息
    else:
        username = input("请输入正确的账号：")
        password = input("请输入正确的密码：")
        # 1. 输入成功， 欢迎用户的名字 使用
        # 2. 失败，重新输入，并显示账号或密码错误,并显示还有几次尝试的机会
        # 3. 如果三次都失败，则五分钟之后再尝试
        if username == user_data:
            if password == password_data:
                print("登录成功，欢迎%s使用~~"%(username))
                break

        else:
            print("账号或密码错误，请重新输入，您还有",count,"次尝试的机会")
# while True 使用案例
# 1.可实现for循环+range功能
# 2.可给特定的条件（比如说账号密码一样）


# In[2]:


word = "bottles"
for beer_num in range(99,0,-1):
    # 吧台靓仔讲
    print(beer_num,"瓶",word,"在啤酒柜上")
    print(beer_num,word,"：瓶")
    print("Take one down")
    print("Pass it around")
    # 客户
    if beer_num == 1:
        print("没有更多的雪花啤酒了")
    else:
        new_num = beer_num - 1
if new_num == 1:
    word = "bottles"
    print(beer_num,"瓶",word,"在啤酒柜上")
    print()


# In[2]:


print("今天要上的课如下")
import datetime
time = datetime.datetime.today().weekday()
count = 3
while True:
    count -= 1
    if count == -1:
        print("连错三次，今天星期几都不知道，真是个笨蛋~")
    else:
        week_time = int(input("今天星期几（请输入0-6的数字）："))
        if week_time == int(time):
            print(time)
            answer = "今天星期{}".format((week_time)+1)
            print(answer)
            if week_time == 0:
                print("星期一早上没课，下午有两节课")
                print("8-10Python语言")
                print("12-13大学英语")

            elif week_time == 1:
                print("毛概实践、H5、定向越野、毛概理论")
            elif week_time == 2:
                print("大学英语、创业实践")
            elif week_time == 3:
                print("Python数据可视化")
            elif week_time == 4:
                print("Illustrator软件应用")
            else:
                print("快乐周末！")
            print("the end")
            break
        else:
            print("今天星期几都不知道吗？您还有", count, "次尝试的机会")


# # week05数据结构之列表
# * 用户输入补充
# * 知识点_列表(list)
# 1. <b>列表的定义：</b>列表是最常用的Python数据类型，列表是可变对象，可以存放0至多个元素(即列表的成员，也是对象)。列表是一个有序的序列，序列中的每个元素都分配一个索引，第一个索引是0，第二个索引是1，依此类推。列表的元素可以插入、增加、删除、修改。常见的操作有索引，切片，加，乘，检查成员等。python已经内置确定列表长度以及确定列表元素最大值、最小值的方法。
# 2. <b>列表的创建：</b>
#   * 空列表，一对圆括号。
#   * 1个元素的列表，用方括号将这个元素包围。
#   * 多个元素的列表，用方括号将多个元素包围，同时元素之间用逗号隔开。
# * 知识点_list(切片)
#  <b>一是索引从0开始，二是左开右闭</b>

# In[3]:


# week05数据结构之列表
# 补充用户信息：打印（print）
# input-> str 如果想让输入的数据类型变成int 需要强制转变数据类型
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")
# info = '''---------INFO'''+ name+'''---------'''+'''
# name:’‘’+name+‘’‘
# age:'''+age+'''
# job:'''+job+'''
# salary:'''+salary
# print(info)

# 占位符有顺序！请依次填入内容
# 思考： 如果有很多个位置呢？如果是一个HTML页面需要很多数据来占用位置
#       对顺序要求太苛刻了，容易出错。
# info_02 = '''--------INFO %s --------
# name: %s
# age: %d
# job: %s
# salary: %d
# '''%(name,name,age,job,salary)
# print(info_02)

# .format() 是一个字符串的格式化方法/函数 优化 占位符
# 优势： 1.不需要考虑参数出现的顺序
#       2.多个重复项只需要赋值一次（明确数据输入（如：变量age）和输出（如：打印的HTML_age））
info_03 = '''-------INFO {HTML_name} -------
name: {HTML_name}
age: {HTML_age}job: {HTML_job}salary: {HTML_salary}
'''.format(HTML_age=age,HTML_salary=salary,HTML_job=job,HTML_name=name)
print(info_03)


# In[7]:


# week05:数据结构之列表

# 构建列表 形式 [] 其中元素以 "," 隔开
# 列表是有顺序的一组值，顺序是从 0 位置开始的
squares = [1, 4, 9, 16, 25]
# names_str = "Mike,Mary,Jan,Jack"
user_data_list = ["Cathy","Yangyang","Today","China"]
password_list = [20011122,19910909,20211001,19451001]
user_age = [20,30,0,72]
# ...
# 列表的嵌套
user_data = [["Yangyang",19910909,30],["Cathy",20011122,20]]

# 应用：请取出每一个名字（如取第一个名字）
# print(names_str[0])

print(user_data_list[0])
print(password_list[0])
print(user_age[0])
print(user_data[0])


# In[8]:


# week05：数据结构之列表
#                  -4，-3，-2，-1,0,1,2,3

names = ["Mike","Mary","Jan","Jack"]
# 知识点 slices（切片）数据是之 values在list中的位置

# 取值 index索引（单个值）  and slice切片（多个或者单个）
# 1. 正数（正向取值，从左到右）
print(names[3])
# 2. 负数（反向取值，从右到左）
print(names[-4])

# 切片
# print(names[5])
# IndexError: list index out of range
print(names[:])
# 1. 在从左往右取值时，右边的值取不到
print(names[1:3])
# 如果从0开始取值，0 可省略不写
print(names[:3])

# 2. 在从右往左取值时,右边的值取不到
print(names[-3:-1])

# 怎么能取到-1这个位置的值呢？ 右侧不写任何值
print(names[-3:])
#
# 3. 特殊情况 可以指定 slice 切片的步长 step
num_list = list(range(10))
print(num_list)
print(num_list[0:7:3])
print(num_list[0:4:3])


# In[ ]:




