print("############################")
print("crossin python exercise: https://res.crossincode.com/wechat/exercise.html")
print("############################")

#1. 输出hello world
print("#######1. 输出hello world########")

print("hello world")

#2. 两数相加
print("#######2. 两数相加########")

a = eval(input('输入加数1：'));
b = eval(input('输入加数2：'));
print("%d + %d = %d"%(a,b,a+b))

#3. 输出1到100
print("#######3. 输出1到100########")
'''
for i in range(1,101):
    print(i+" ")
'''
print(list(range(1,101)))

#4. 1加到100的和
print("#######4. 1加到100的和########")
'''
sum = 0;
for i in range(1,101):
    sum += i;
print(sum)
'''
from functools import reduce
print(reduce(lambda x,y:x+y, range(1,101)))

#5. 等比数列
print("#######5. 等比数列########")
n = eval(input('输入公比(>1)：'))
print("%d为公比，首项为1的等比数列前10项：" % n)
'''
num = 1;
for i in range(0,10):
    print(num);
    num = num * n;
'''
print([n**i for i in range(0,10)])

#6. 输出斐波那契数列
print("#######6. 输出斐波那契数列########")
list1 = [1,1]
count = eval(input('输入斐波那契数列个数(>1)：'))
i=1
'''
while i<count-1:
    list1.append(list1[i-1]+list1[i])
    i = i+1
'''
for i in range(count-2):
    list1.append(list1[-2]+list1[-1])
print(list1)

#7. 输出三角形
print("#######7. 输出三角形########")
'''
   *
  * *
 * * *
* * * *
'''
n = eval(input('输入底边星号数：'))
for row in range(n): #[0,n-1]
    for col_blank in range(n-row-1):
        print(' ',end='') #end=''作用是实现同行输出；print('any to output'),逗号实现同行输出并输出空格的作用在python3无效
    for col_star in range(row+1):
        print('* ', end='')
    #print('\n')
    print()

#8. 输出乘法表
print("#######8. 输出乘法表########")
for mul_1 in range(1,10):
    for mul_2 in range(1,mul_1+1):
        print('%d * %d = %d\t'%(mul_2, mul_1, mul_1*mul_2), end='')
    print()

#9. 求最大值
print("#######9. 求最大值########")
print("输入一串数字（间以空格）：")
print(max([int(x) for x in input().split()]))

#10. 除3且除5且除7余2的数
print("#######10. 除3且除5且除7余2的数########")
for i in range(1,1001):
    if(i%3 == 2 and i%5 ==2 and i%7==2):
        print(i, end=' ')
print()

#11. 回文数
print("#######11. 回文数########")
for i in range(1,201):
    i2_str = str(i**2)
    if(i2_str == i2_str[::-1]):
        print(i, end=' ')
print()

#方法2
for i in range(1,201):
    i2_list = []
    for j in str(i**2):
        i2_list.append(j)
    i2_list.reverse()  #i2_list is reversed now
    if(str(i**2) == ''.join(i2_list)):
        print(i, end=' ')
print()


#12. 提取英文单词
print("#######12. 提取英文单词########")
#_*_coding=utf-8_*_
import re

with open('from.txt') as f: #使用with语句，可以确保在发生或不发生异常的情况下，都能正确关闭文件，释放资源
    data = f.read()

word_in_data = re.findall('[A-z]+',data)
word_in_data.sort()
data = ' '.join(word_in_data)

with open('to.txt', 'w') as f:
    f.write(data)


#13. 查询热映电影
