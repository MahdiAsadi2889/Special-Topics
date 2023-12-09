a = ['m', 'na']
b = ['y', 'me']
c = []
for i, j in zip(a, b):
    for x,y in i,j:
        c.append(x+y)
print(c)
