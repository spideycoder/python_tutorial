print("Enter a integer")
a = int(input())


def check_prime(b):
    for j in range(2, b):
        if b % j == 0:
            return "Not prime"
    return "Prime"

check_prime(a)
