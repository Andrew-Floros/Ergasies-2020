num = int(input("Enter Integer "))
last_digit = 0
digit_sum = 0
num = 3*num
num = num + 1 
while num > 0:
    last_digit = num%10
    digit_sum = digit_sum + last_digit
    num = num//10
    flag=num
    if flag == 0 and digit_sum >= 10: 
      num = digit_sum
      num = 3*num
      num =  num + 1
      digit_sum = 0 
print(digit_sum)



