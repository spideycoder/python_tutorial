a = [1,4,6,8,1,12,9]
[1,4,6,1, 8,9,12]
[1,4,1,6, 8,9,12]
b = 0
while not b:
    b=1
    for i in range(len(a)-1):
            b *= a[i+1]<a[i]

            a[i+1],a[i] = max(a[i],a[i+1]), min(a[i],a[i+1])

print(a)
#
# a = -10
#
# b = -20
#
# # a= a+b
# # b= a-b
# # a= a -b
#
#
# a,b = b, a
# print(a,b)