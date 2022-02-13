def prime(n):
    i = 0
    j = 2
    while(i<n):
        if(j==2):
            yield j
        else:
            for k in range(2,j):
                if j%k == 0:
                    break
            else:
                i += 1
                yield(j)
        j += 1

f = prime(10)

for i in range(10):
    print(next(f))