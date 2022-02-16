def is_prime(number):
    i = 2
    while i*i <= number:
        if number%i==0:
            return 0
        i+=1
    return 1