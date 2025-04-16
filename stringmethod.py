str1= input()
for i in range(len(str1)):
    if i==0 or i==len(str1)-1 or str1[i+1] == " " or str1[i+1]==" " :
        print(str1[i].upper(),end="")
    else:
        print(str1[i], end="")
    




#input: Take U Forward is Awesome
#output: TakE U ForwarD iS AwesomE


#input:take u forword is awesome
#output:TakE U forworD iS awesomE
