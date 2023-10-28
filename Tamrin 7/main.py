def countDown(first,second):
    if first == 0:
        print("Stop !!!")
    else:
        print(first)
        print(second)
        countDown(first-second,second)
print(countDown(9,3))