import time

start=time.time()
a = 1
b =[""]*a

def fib(a,b):

    if a == 0:

        b[a] = 0
        return 0
    elif a == 1:

        b[a] = 1
        return 1
    else:
        # if(b==0):
            # print(fib(a - 1,1) + fib(a - 2,1))

        if b[a] == "":
            b[a]= fib(a-2,b)+fib(a-1,b)
        return fib(a-2,b)+fib(a-1,b)
fib(a-1,b)
print(b)
end = time.time()
print(end -start)
print(kanta)
kanta =4