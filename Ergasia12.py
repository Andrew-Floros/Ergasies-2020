import datetime
today= datetime.datetime.today()
day = int(input('Enter a day:'))
month = int(input('Enter a month:'))
year = int(input('Enter a year:'))
date = datetime.datetime(year,month,day)
delta=date-today
hours=int(delta.seconds/3600)
seconds=delta.seconds-3600*hours
print( "It's " ,delta.days,"days  ",int(hours), "hours  ",seconds,"seconds ","until then")
if month==2:
  if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("The inserted month has 29 days")
       else:
           print("The inserted month has 28days")
   else:
       print("The inserted month has 29 days")
  else:
    print("The inserted month has 28 days")
elif month==4 or month==6 or month==9 or month==11 :
	print("The inserted month has 30 days")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
	print("The inserted month has 31 days")