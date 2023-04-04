# Basic - Print all integers from 0 to 150.
for x in range (0,151):
    print(x)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1000,5):
    print(x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range (1,100):
    print (y)
    if y % 5 == 0:
        print("Coding")
    if y % 10 == 0:
        print("Coding Dojo")
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for i in range (0, 500000):
    sum += i
print (sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for m in range (2018,0,-4):
    print(m)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for k in range (lowNum,highNum):
    if k % mult == 0:
        print(k)