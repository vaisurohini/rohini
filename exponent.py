define power(base,exponent):
    if(exponent==1):
        return(base);
    if(exponent!=1):
        return(base*power(base,exponent-1));
base=int(input("Enter the base: "));
exponent=int(input("Enter exponential value: "));
print(" The result:",power(base,exponent));
