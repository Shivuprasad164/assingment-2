string=input("enter the sentence:")

for i in string.split():
    first_char=i[0].upper()
    last_char=i[-1].upper()
    i=first_char +i[1:-1] + last_char
    print(i,end=" ")