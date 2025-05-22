# A,B = map(int,input().split())
# if -10000 <= A <= 10000 and -10000 <= B <= 10000:
#     if A > B:
#         print(">")
#     elif A < B:
#         print("<")
#     else:
#         print("==")


# score = int(input())
# if 0 <= score <= 59:
#     print("F")
# if 60 <= score <= 69:
#     print("D")
# if 70 <= score <= 79:
#     print("C")
# if 80 <= score <= 89:
#     print("B")
# if 90 <= score <= 100:
#     print("A")

# a,b = map(int,input().split())
# if a>0 and b>0:
#     print("1사분면")
# if a>0 and b<0:
#     print("4사분면")
# if a<0 and b>0:
#     print("2사분면")
# if a<0 and b<0:
#     print("3사분면")


# year = int(input())
# if (year %4 == 0 and year %100 != 0) or (year %400 == 0):
#     print("1")
# else:
#     print("0")


# N,M = map(int,input().split())
# print(abs(N-M))


import random


a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)

if a == b == c:
    prize = 10000+a*1000
elif a == b or a == c:
    prize = 1000+a*100
elif b == c:
    prize = max(a,b,c)*100
    
print("상금:",prize)
    
