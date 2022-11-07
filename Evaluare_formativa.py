import datetime
#with open("Produse.IN.txt",'r') as f:
    #nr_alimente = f.readline()
    #denumiri = tuple(f.readline())
    #data_fabricarii = tuple(f.readline())
    #data_expirarii = tuple(f.readline())
    #pret_initial = tuple(f.readline())

nr_alimente=3
denumiri = ('paine', 'lapte', 'pizza')
data_fabricarii= ('6.11.2022', '1.10.2022', '7.11.2022')
data_expirarii = ('8.11.2022', '12.11.2022', '7.11.2023')
valabilitate1 = []
valabilitate2 = []
pret_initial = (5, 12, 20)
pret_actual = [0,0,0]
data_curenta = datetime.date.today()
catalog = {}

for i in range(nr_alimente):
    data_fabricare_i = data_fabricarii[i]
    data_expirare_i = data_expirarii[i]
    catalog[denumiri[i]]={'fabricare':data_fabricare_i.split('.'),'expirare':data_expirare_i.split('.')}

zi=data_curenta.day
luna=data_curenta.month
an=data_curenta.year

for i in range(nr_alimente):
    if int(an)<=int(catalog[denumiri[i]]['expirare'][2]):
        if int(luna)<=int(catalog[denumiri[i]]['expirare'][1]):
            if int(zi)<=int(catalog[denumiri[i]]['expirare'][0]):
                valabilitate1.append(str(int(catalog[denumiri[i]]['expirare'][0])-int(catalog[denumiri[i]]['fabricare'][0])))
                valabilitate2.append(str(int(catalog[denumiri[i]]['expirare'][0])-int(zi)))
                if catalog[denumiri[i]]['expirare'][1]!=catalog[denumiri[i]]['fabricare'][1]:
                    valabilitate1[i]+='.'+str(int(catalog[denumiri[i]]['expirare'][1])-int(catalog[denumiri[i]]['fabricare'][1]))
                    if catalog[denumiri[i]]['expirare'][2]!=catalog[denumiri[i]]['fabricare'][2]:
                        valabilitate1[i]+='.'+str(int(catalog[denumiri[i]]['expirare'][2])-int(catalog[denumiri[i]]['fabricare'][2]))
                if int(catalog[denumiri[i]]['expirare'][1])!=int(luna):
                    valabilitate2[i]+='.'+str(int(catalog[denumiri[i]]['expirare'][1])-int(luna))
                    if int(catalog[denumiri[i]]['expirare'][2])!=int(an):
                        valabilitate2[i]+='.'+str(int(catalog[denumiri[i]]['expirare'][2])-int(an))
                else:
                    if catalog[denumiri[i]]['expirare'][2]!=catalog[denumiri[i]]['fabricare'][2]:
                        valabilitate1[i]+='.'+'0'+'.'+str(int(catalog[denumiri[i]]['expirare'][2])-int(catalog[denumiri[i]]['fabricare'][2]))
                    if int(catalog[denumiri[i]]['expirare'][2])!=int(an):
                        valabilitate2[i]+='.'+'0'+'.'+str(int(catalog[denumiri[i]]['expirare'][2])-int(an))

for i in range(nr_alimente):
    if len(valabilitate1)!=nr_alimente:
        n=3-len(valabilitate1)
        for j in range(n):
            valabilitate1.append('0')
    if len(valabilitate2)!=nr_alimente:
        n=3-len(valabilitate2)
        for j in range(n):
            valabilitate2.append('0')

list_50_reducere=[]
list_20_reducere=[]
list_1an_valabil=[]
list_1luna_valabil=[]

for i in range(nr_alimente):
    list1 = valabilitate1[i].split('.')
    list2 = valabilitate2[i].split('.')
    if len(list1)!=nr_alimente:
        n=3-len(list1)
        for j in range(n):
            list1.append(0)
    if len(list2)!=nr_alimente:
        n=3-len(list2)
        for j in range(n):
            list2.append(0)
    zile1 = int(list1[0])+int(list1[1])*30+int(list1[2])*365
    if zile1>=365:
        list_1an_valabil.append(denumiri[i])
    if zile1<=30 and zile1>0:
        list_1luna_valabil.append(denumiri[i])
    zile2 = int(list2[0])+int(list2[1])*30+int(list2[2])*365
    if zile2>zile1/2:
        pret_actual[i]=pret_initial[i]
    if (zile2<=zile1/2) and (zile2>(zile1/2)-(zile1/4)):
        pret_actual[i]=pret_initial[i]-(pret_initial[i]/5)
        list_20_reducere.append(denumiri[i])
    if zile2<=zile1/4 and zile2>0:
        pret_actual[i]=pret_initial[i]/2
        list_50_reducere.append(denumiri[i])
    if zile2==0:
        pret_actual[i]=0

lista_expirate=[]

for i in range(nr_alimente):
    if int(catalog[denumiri[i]]['expirare'][0])<=int(zi) and int(catalog[denumiri[i]]['expirare'][1])<=int(luna) and int(catalog[denumiri[i]]['expirare'][2])<=int(an):
        lista_expirate.append(denumiri[i])
print('lista produselor cu termen de valabilitate expirat: ',lista_expirate)
print('lista produselor cu o reducere la pret de 50%: ',list_50_reducere)
print('lista produselor cu o reducere la pret de 20%: ',list_20_reducere)
print('lista produselor cu termenul de valabilitate de cel putin un an: ',list_1an_valabil)
print('lista produselor cu termenul de valabilitate de cel mult o luna: ',list_1luna_valabil)