def clist():
    l,l1,l2=[],[],[]
    for i in range(1,10):
        l.append(i)
    for i in range(10,1,-2):
        l1.append(len(l1))
    for i in range(len(l1)):
        l2.append(l1[i]+l[i])
    l2.append(len(l)-len(l1))
    print(l)
    print(l1)
    print(l2)
clist()
