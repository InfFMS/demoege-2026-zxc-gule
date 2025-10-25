n=0
r=0
t=0
for i in range(1,100):
    n=bin(i)[2:]
    if i%3==0:
        n+=bin(i)[-1:-3]
        r=int(n,2)
        if r>200:
            print(r,i)
            break
    else:
        t=bin((i%3)*3)[2:]
        n+=t
        r=int(n,2)
        if r>200:
            print(r,i)
            break
print('Ответ:',i)