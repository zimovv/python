#crossin python exercise: https://res.crossincode.com/wechat/exercise.html

#1. 输出hello world
print("hello world")

#2. 两数相加
'''
print("输入加数1：")
a = eval(input());
print("输入加数2：")
b = eval(input());
print("%d + %d = %d"%(a,b,a+b))
'''

#3. 输出1到100
'''
for i in range(1,101):
    print(i+" ")
'''
print(list(range(1,101)))

#4. 1加到100的和
'''
sum = 0;
for i in range(1,101):
    sum += i;
print(sum)
'''
from functools import reduce
print(reduce(lambda x,y:x+y, range(1,101)))

#5. 等比数列
print("输入公比：")
n = eval(input())
print("%d为公比，首项为1的等比数列前10项：" % n)
'''
num = 1;
for i in range(0,10):
    print(num);
    num = num * n;
'''
print([n**i for i in range(0,10)])

#6. 输出斐波那契数列

#7. 输出三角形

#8. 输出乘法表

#9. 求最大值

#10. 除3、5/7余2的数

#11. 回文数

#12. 提取英文单词

#13. 查询热映电影
