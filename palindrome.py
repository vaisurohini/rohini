n=int(input("Enter the number:"));
temp=n
rev=0:
while(n>0):
    dig=n%10
    rev=rev*10+dig;
    n=n//10;
if(temp==rev):
    print("Enter the number is a palindrome:!");
else:
    print("Enter the number is not a palindrome:!");
