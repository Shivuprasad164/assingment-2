string=input("enter any string:")
for i in string:
    if(i == '@' or i == '#' or i == '$' or i == '^' or i == '&' or i == '*'
       or i == '?'):
     print ("string is not accepted")
     break
else:
    print ("string is accepted")