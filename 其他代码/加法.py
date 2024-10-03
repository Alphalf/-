#give @s crossbow{Enchantments:[{id:'unbreaking',lvl:10},{id:'piercing',lvl:10}，{id:'mending',lvl:10},{id:'quick_charge',lvl:5},{id:'multishot',lvl:10}]}
from math import fabs           #导入数学模块
from time import perf_counter   #导入时间模块

def Bar(i):         #动态文本条
N = pow(10,level)
a = int((i/N)*50)
b = 50 - a
Y , N = '*' * a , '.' * b
print("\r计算中：{:3.0f}% [{}->{}] {:.2f}s".format(2*a,Y,N,perf_counter()),end='')
level = eval(input('计算Pi精确到小数点后几位数：'))
print('\n{:=^70}'.format('计算开始'))
a,b,pi,tmp = 1,1,0,1
i = 0
'''
a 分子  |  b 分母  |  pi 圆周率
18 tmp 存储a/b的值    |  i  执行进度
19 '''
20 perf_counter()      #开始计时
21 while (fabs(tmp) >= pow(10,-level)): #计算Pi
22     pi += tmp
23     b += 2
24     a = -a
25     tmp = a/b
26     i += 2
27     Bar(i)          #调用函数，实时显示计算进度
28
29 print('\n{:=^70}'.format('计算完成'))
30 print('\nPi的计算值为：{}'.format(round(pi*4,level))) #输出计算结果


