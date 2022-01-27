#Q1
def isvowel(c):
    return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', "I", 'O', 'U']
 
def isletter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'
 
def isconsonant(c):
    return  not isvowel(c) and isletter(c)
 
def vccounts(s):
    a = list(s.lower())
    au = set(a)
    return sum([isvowel(c) for c in a]), sum([isconsonant(c) for c in a]), \
        sum([isvowel(c) for c in au]), sum([isconsonant(c) for c in au])
 
def testvccount():
    teststrings = [
        "ABABCOSCNcancaspwnsm",
        "Now is the time for all good men to come to the aid of their country."]
    for s in teststrings:
        vcnt, ccnt, vu, cu = vccounts(s)
        return True if vcnt > ccnt:
            else False
#Q2
import math
#take radius of the base of  a cylinder from user
r=float(input("Enter r of a cylinde"))
#take height of the curve surface of a cylinder from user
h=float(input("Enter the Height of a cylinde"))
#calculate the surface area of cylinder
s_area=2*math.pi*pow(r,2)*h
#calculate the volume of cylinder
volume=math.pi*pow(r,2)*h
print("surface area of a cylinder wll be %.2f" %s_area)
print("volume of a cylinder will be  %.2f" %volume)

#Q3
strings = ['do', 're', 'mi']
','.join(strings)

#Q4
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

lst = []

lst.append(l1)
lst.append(l2)
lst.append(l3)
print(lst)

#Q5