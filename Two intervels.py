lower = 100
upper = 2000
for num i range(lower, upper +1):
print("enter the lower and upper number:")
   order = len(str(num))
sum = 0
temp = 0
   while temp > 0:
      digit = temp %10
      sum +=digit**order
      temp//=10
      if num==sum:
      print(num)
   
