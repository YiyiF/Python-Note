def print_max(x,y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    #如果可能，都将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)

#通过help（)函数可以获取函数的_doc_属性并以一种
#   整洁的方式将其呈现 e.g. help(print_max)