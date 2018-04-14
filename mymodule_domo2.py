from mymodule import say_hi,__version__

say_hi()
print('Version',__version__)

#但推荐使用import语句，避免模块里名称冲突