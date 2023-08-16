def prime_number(number):
    if number == 1:
        return True
    elif number == 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


while True:
    print("Press 'g' to exit")
    a = input("Please enter the number:")
    if a == "g":
        break
    else:
        a = int(a)
        if prime_number(a):
            print("Prime number")
        else:
            print("Not a prime number")
