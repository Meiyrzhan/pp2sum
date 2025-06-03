#Exercise 1--------------------------------------------------------------------------------
import math
last = [1,2,3,4,5,69,7,8,9,0]

print(math.prod(last))
#Exercise 2--------------------------------------------------------------------------------
text = "I love money and my mom."

up = sum([1 for i in text if i.isupper()])
low = sum([1 for i in text if i.islower()])

print( up, low)
#Exercise 3--------------------------------------------------------------------------------
def pal(s):
    if s == s[::-1]:
        return True
    else:
        return False
text1 = "NON"
text2 = "NAGGA"

print(pal(text1))
print(pal(text2))
#Exercise 4--------------------------------------------------------------------------------
import time
def uahah(num,time):
    time.sleep(time/1000)
    return(num**2)
num = int(input())
time = int(input())

print(uahah(num,time)
#Exercise 5--------------------------------------------------------------------------------
