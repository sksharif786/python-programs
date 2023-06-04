n=int(input("entere the decimal number"))
l=list()
while n!=0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()
for ele in l:
    print(ele,end="")    