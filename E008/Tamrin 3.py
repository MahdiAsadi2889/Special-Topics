a = "b", "C", "l", "#", "@"
l1 = []
l2 = []
l3 = []
for i in range(len(a)):
    if a[i].islower():
        l1.append(a[i])
    elif a[i].isupper():
        l2.append(a[i])
    else:
        l3.append(a[i])
print("L1 is : ", l1)
print("L2 is : ", l2)
print("L3 is : ", l3)
