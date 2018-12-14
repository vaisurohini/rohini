# Python Program - Check Alphabet or Not

print("Enter '0' for exit.");
ch = input("Enter the any character: ");
if ch == '0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print("the given character",ch, "is an alphabet.");
    else:
    	print("the given character", ch, "is not an alphabet.");
