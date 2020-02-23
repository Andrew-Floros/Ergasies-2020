temp=0
temp1=0
temp2=0
last_digit=0
sum=0
flag=0
while flag==0:
  cardnumber=int(input("Enter a 16-digit credit card number:"))
  if cardnumber<=9999999999999999 and cardnumber>=1000000000000000:
    break
  else:
    print("Try Again!")  
cardnumber=str(cardnumber)
crednum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,16):
  crednum[i]=int(cardnumber[i])
for i in range (0,16,2):
    crednum[i]=crednum[i]*2
    temp1=crednum[i]
    if temp1>9:
      last_digit=temp1%10
      temp2=temp2+last_digit
      temp1=temp1//10
      last_digit=temp1%10
      temp2=temp2+last_digit
      temp1=temp1//10
      crednum[i]=temp2  
      temp2=0
for i in range (0,16):
 sum = sum + crednum[i]
if sum%10==0:
  print("Credit card number is valid")
else :
  print("Credit card number is invalid") 