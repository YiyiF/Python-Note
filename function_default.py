def say(message,times=1):
    print(message*times)

say('Hello')
say('World',5)

#注意：
#只有位于参数列表末尾的参数才能被赋予默认参数值，
#即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的前面
#e.g. def func(a,b=5)有效，而def func(a=5,b)无效