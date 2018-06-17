#get M number from N number

N=100
M=10
import random
l = random.sample(range(1,N),M)
print(l)


l.append(200)
l2 = [12,23,23,12,33,23]
#sorted and no duplicated
s = sorted(set(l+l2))
print(s)
