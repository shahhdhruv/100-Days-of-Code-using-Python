# Which year do you want to check?
year = int(input())

if (year % 4 == 0) and (year % 400 == 0) and (year % 100 != 0 ):
  print("Leap Year")
else:
  print("Not Leap Year")
