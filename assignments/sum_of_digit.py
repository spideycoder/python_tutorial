print("Enter a interger between 1000 and 1000000")
a = int(input())
b = 0
while(a>=1):
    b= b + (a % 10)
    print("b",b)
    #a=(a-(a%10))/10 # removing last digit
    a = a//10
    print("a",a)
print("Sum of digit = ",b)

