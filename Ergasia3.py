i=int(input("number"))
myDict = {} 
for z in range(i):
  myDict[z] = [str(input("What did you  purchase? ")),int(input("Item Quantity ")), float(input(" Enter Item Price in Euros (not inlcuding tax)  ")) , int(input("Enter Item Tax Percentage "))]  
def cost(list):
  payment= list[2]*list[3]/100 + list[2]
  payment=payment*list[1]
  print ("The", list[1],list[0],"(s)","cost", payment, "euros")
for z in range(i):   
  cost(myDict[z])   