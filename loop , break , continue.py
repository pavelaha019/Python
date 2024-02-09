
n = int(input("Enter the last term : "))
'''
i = 1
while i <= 100:
    print(i)
    i+=1
print("Program end")

sum = 0
i = 1
while i <= n:
    sum = sum + i
    i=i+1

print("Sum is " , sum)


#Break
i = 1
while i <= n:
    if i == 20 :
        break
    print(i)
    i=i+1
'''
#Continue

i = 1
while i <= n:
    if i == 20 :
        continue
    print(i)
    i=i+1