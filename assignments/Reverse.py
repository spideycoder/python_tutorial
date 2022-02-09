print("enter any number")
a = input()
b = ""

for i in range(len(a)):
   b = b[:i] + a[-i-1]
print(b)

a = [1, 2, 3, 4]
print(a[::-2])
