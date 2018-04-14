#可变参数
def total(a=5,*numbers,**phonebook):
    print('a',a)

    #遍历元组中的所有项目
    for singe_item in numbers:
        print('single item',singe_item)

    #遍历字典中的所有项目
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


#声明一个*param的参数时，从此处开始直至结束的所有位置参数
#都将被收集被汇集成一个成为‘param’的元组（Tuple）

#声明一个**param的参数时，从此处开始直至结束的所有关键字参数
#都将被收集被汇集成一个名为param的字典（Dictionary）