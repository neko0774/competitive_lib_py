def is_prime(number):
<<<<<<< HEAD
    if number < 2: return 0
    if number==2: return 1
    if number%2==0: return 0
=======
    if i < 2: return 0
    if i==2: return 1
    if i%2==0: return 0
>>>>>>> 851f48418d8354176a5edee1f1b66ff9943f9366
    i = 3
    while i*i <= number:
        if number%i==0:
            return 0
        i+=2
<<<<<<< HEAD
    return 1
=======
    return 1
>>>>>>> 851f48418d8354176a5edee1f1b66ff9943f9366
