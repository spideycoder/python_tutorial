a,b=(2,2.0)
if(a>b):
    print("a is greater than b")
elif(a==b):
    print("a is equal to b")
else:
    print("a is smaller than b")

## Grade calculator

marks = 50
if(marks>=80):
    print("You got A")
elif(marks>=60):
    print("You got B")
elif(marks>=30):
    print("You got C")
else:
    print("You fail loser")

## Driving license
## 1 age 2 Nationality 3 Pass
age = 21
nationality = "Indian"
test = True
if(age<18):
    print("You are under-aged")
elif(nationality!="Indian"):
    print("Not an Indian")

## Brahmin categorisation
region = "North"
caste = "brahmin"

if(caste=="brahmin") and  (region=="North"):
    print("OG")
elif(caste=="brahmin") and (region == "South"):
    print("Half pseudo Brahmin")
elif(caste=="brahmin") and (region=="Marathi"):
    print("Psudo Brahmin")
else:
    print("NA")
