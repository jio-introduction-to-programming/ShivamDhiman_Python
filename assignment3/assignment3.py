#Question 1
lst1 = [1, 2, 3, 4, 5]
total = 0
for n1 in lst1:
    if n1 == 3:
        break
    total += n1
print("Answer1:",total)

#------------------------------------------
#Question 2

lst2 = [1, 2, 3, 4, 5]
for n2 in lst2:
    if n2 % 2 == 0:
        continue
print("Answer2:",n2)

#------------------------------------------
#Question 3

i3 = 0
while i3 < 5:
    if i3 == 3:
        break
    i3 += 1
print("Answer3:",i3)

#------------------------------------------
#Question 4

x4 = 10
y4 = 5
if x4 > y4:
    print("Answer 4:","x is greater than y")
elif x4 == y4:
    print("Answer 4:","x is equal to y")
else:
    print("Answer 4:","x is less than y")

#------------------------------------------
#Question 5

i5 = 0
while i5 < 5:
    i5 += 1
    if i5 == 3:
        continue
print("Answer 5:",i5, end=' ')
print()
#------------------------------------------
#Question 6


n6 = [1, 2, 3, 4, 5]
total = 0
for num6 in n6:
    if num6 % 2 != 0:
        total += num6
print("Answer 6:",total)

#------------------------------------------
#Question 7

x = 5
y = 3
if x > y:
    if x % y == 0:
        print("Answer 7:","x is divisible by y")
    else:
        print("Answer 7:","x is not divisible by y")
else:
    print("Invalid comparison")

#------------------------------------------
#Question 8

n8 = [1, 2, 3, 4, 5]
for num8 in n8:
    if num8 % 2 == 0:
        break
    print("Ans 8:",num8)
else:
    print("Ans 8: All numbers are even")

#------------------------------------------
#Question 9

i9 = 0
print("Answer 9:",end=" ")
while i9 < 5:
    i9 += 1
    if i9 == 3:
        continue
    print(i9, end=' ')
else:
    if i9== 5:
        print("Loop completed successfully", end=' ')

#------------------------------------------
#Question 10

print("")
x10 = 100
print("Answer 10 : ",end=" ")
while x10 > 0:
    print(x10, end=' ')
    x10 = x10 // 2