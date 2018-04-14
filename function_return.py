def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2,3))

#return语句如果没有搭配任何一个值则代表
#   返回None（虚无）

#每一个函数都在其末尾隐含了一句 return None
#  除非写了自己的 return语句

#可以运行print（some_function()）,
#   其中some_function函数不使用return语句
# def some_function()
#   pass

#！   pass语句用于指示一个没有内容的语句块
