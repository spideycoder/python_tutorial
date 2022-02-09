print("enter N and Q")
(N,Q)=(int(input()),int(input()))
print(N,Q)
a =[]
P= [0]*N

for i in range(1,Q+1):
    print("enter ",i," command")
    a.append([int(input()),int(input()),int(input())])
    #a[i]=[int(input()),int(input()),int(input())]
    print(a)
print(a[1][1])

for j in range(Q):
    heads =0
    if(a[j][0]==0):
        for k in range(a[j][1],a[j][2]+1):
            P[k]=1
    else:
        for l in range(a[j][1], a[j][2]+1):
            heads+=P[l]
        print(heads)

print(P)