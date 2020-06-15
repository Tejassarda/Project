

print("                         Welcome to Pizza Hub")


pizzas=["0.Onion Pizza-Rs.100","1.Capsicum Pizza-Rs.120","2.Paneer Pizza-Rs.150","3.Mexican Pizza-Rs.180"]
lst1=[]
lst2=[]
lst3=[]
lst4=[]
print("MENU")
for i in pizzas:
    print(i)
while True:
    a=input("Do you want to order anything?,Type Yes or No")
    if (a=="yes" or a=="Yes"):
        order=int(input("What would you like to order Sir?\nPlease enter the item number only."))
        quantity=int(input("please tell the quantity"))
        lst1.append(order)
        lst2.append(quantity)

    elif (a=="no" or a=="No"):
        print("Ok,Thanks for visiting")
        break

for i in lst1:
    if i==0:
        lst3.append(100)
        
    if i==1:
        lst3.append(120)

    if i==2:
        lst3.append(150)

    if i==3:
        lst3.append(180)

counter=0
for i in lst2:
    c=i*lst3[counter]
    lst4.append(c)
    counter+=1

print(lst1)
print(lst2)
print(lst3)
print(lst4)

b=0
for i in lst4:
    b=b+i
print("Your bill total without GST=Rs.",b)
d=((b/100)*18)
print("18% GST=Rs.",d)
e=(b+d)
print("Your final bill with GST sir=Rs.",e)


    
    
    




