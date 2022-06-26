

def prime_checker(number):

    pnum = False

    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                pnum = True
                break

    if pnum:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")



    

n = int(input("Check this number: "))
prime_checker(number=n)