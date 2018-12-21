fileName = input("Enter the file to check: ").strip();

infile = open(enter tha fileName, "r");
vowels = set("A E I O U a e i o u");
consonants = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z");
text = infile.read().split();
countV = 0
for V in text:
    if V in vowels:
      countV += 1
       countC = 0
for C in text:
    if C in consonants:
        countV=0
        countC += 1
print("enter the number of Vowels is: ",countVoewls,"\nenter the number of consonants is: ",count Consonants);
