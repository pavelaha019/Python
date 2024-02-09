#Ternary oparetor 

num1 = 10
num2 = 5
num3 = 2

max = num1 if num1 > num2 else num2
print("Maximum : ",max)
min = num1 if num1 < num2 else num2
print("Minimum : ",min) 

# Logical oparetor

if num1 > num2 and num1 > num3 :
    print("Greater number is ",num1)
elif num2 > num1 and num2 > num1 :
    print("Greater number is ",num2)
else :
    print("Greater number is ",num3)
    
    
ch= 'a'

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print("Vowel")
else :
    print("Consonant")