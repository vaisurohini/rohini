num = int(input("Enter the value of a natural number : "));
hold = num;
sum = 0;

if num <= 0: 
   print("Enter the whole positive number!");
else: 
   while num > 0:
        sum = sum + num;
        num = num - 1;
    print("Sum of first natural number", hold, "natural numbers is: ", sum);
