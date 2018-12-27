
number = int(input("Enter the any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("Enter the number, is not a prime number:");
            break;
    else:
        print("Enter the number, is a prime number:");
else:
    print("Enter the number, is not a prime number:");
