a = int(input("Please Enter the First Number of an A.P Series: "));
n = int(input("Please Enter the Total Numbers in this A.P Series: "));
d = int(input("Please Enter the Common Difference : "));
total = 0:     
value = a:
print("Arithmetic the Progression Series : ", end = " ");
for i in range(n):
    print("%d + " %value, end = " ");
    total = total + value;
    value = value + d;
print("\nThe Sum of Arithmetic Progression Series upto %d = %d " %(n, total));
