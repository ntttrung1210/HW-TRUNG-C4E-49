#Nhap mon an
menu={'name':['com ga','com rang','pho bo','bun bo hue'],'price':[40,20,30,50],'type':['lunch','lunch and breakfast','breakfast','lunch']}
print("Menu")
for i in range(len(menu['name'])):
    print(menu['name'][i],end='\t\t')
    print(menu['price'][i])
print("Cac mon gia <40")
for i in range(len(menu['name'])):
    if menu['price'][i]<40:
        print(menu['name'][i],end='\t\t')
        print(menu['price'][i])
print("Cac mon chi an trua")
for i in range(len(menu['name'])):
    if menu['type'][i]=='lunch':
        print(menu['name'][i],end='\t\t')
        print(menu['price'][i])
cd1=str.upper(input("Do you want to add some food?(Y/N)"))
if cd1=='Y':
    menu['name'].append(input("Nhap ten mon an: "))
    menu['price'].append(input("Nhap gia: "))
    menu['type'].append(input("nhap loai: "))
    for i in range(len(menu['name'])):
        print(menu['name'][i],end='\t\t')
        print(menu['price'][i])
a=str.lower(input("Nhap ten mon an mun xoa: "))
dk=0;
for i in range(len(menu['name'])):
    if a==menu['name'][i]:
        dk=1
        break
if dk==1:
    menu['name'].pop(i)
    menu['price'].pop(i)
    menu['type'].pop(i)
    for i in range(len(menu['name'])):
        print(menu['name'][i],end='\t\t')
        print(menu['price'][i])
else: print("khong co mon an do")
#Nen chuoi
a=str.lower(input("Nhap chuoi: "))
k=[]
for i in range(len(a)):
    k.append(a[i])
k.append(' ')
i=0
while i!=len(k)-1:
    for j in range(i+1,len(k)):
        if k[i]!=k[j]:
            if j-i!=1:
                print(str(k[i])+'['+str(j-i)+']',end='')
                i=j
                break
            else:
                print(str(k[i]),end='')
                i=j
                break
#Exercise 1
inventory={'gold':500,'pounch':['flint','twine','gemstone'],'backpack':['xylophone','dagger','bedroll','bread loaf']}
inventory.update({'pocket':['seashell','strange berry','lint']})
del inventory['backpack'][1]
inventory['gold']=inventory['gold']+50
print(inventory['gold'])
Exercise 2
prices={'banana':4,'apple':2,'orange':1.5,'pear':3}
stock=prices.copy()
stock['banana']=6
stock['apple']=0
stock['orange']=32
stock['pear']=15
for i in prices:
    print(i)
    print('price: '+str(prices[i]))
    print('stock: '+str(stock[i]))
total=0
for i in prices:
    total=total+prices[i]*stock[i]
print(total)
Exercise 3
op='Y'
a=[35,36,40,44]
while True:
    print("Answer the following algebra question:",end='\n')
    print("If x=8, then what is the value of 4(x+3) ?",end='\n')
    for i in range(len(a)):
        print(str(i+1)+'. '+str(a[i]),end='\n')
    b=int(input('Your choice: '))
    if b==4:
       print("Bingo")
    else:
       print(":(")
    op=str.upper(input("DO you want to continue?(Y/N)"))
    if op=='N':
        break
#Exercise 4
a=[35,36,40,44]
print("Answer the following algebra question:",end='\n')
print("If x=8, then what is the value of 4(x+3) ?",end='\n')
dem=0
for i in range(len(a)):
    print(str(i+1)+'. '+str(a[i]),end='\n')
b=int(input('Your choice: '))
if b==4:
   print("Bingo",end='\n')
   dem=dem+1
else:
   print(":(",end='\n')
print("Estimate this answer (exact calculation not needed)",end='\n')
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mea n!",end='\n')
a=['About 55','About 65','About 75','About 85']
for i in range(len(a)):
    print(str(i+1)+'. '+str(a[i]),end='\n')
b=int(input('Your choice: '))
if b==2:
   print("Bingo",end='\n')
   dem=dem+1
else:
   print(":(",end='\n')
print("You correctly answer "+str(dem)+" out of 2 questions")









    
        



