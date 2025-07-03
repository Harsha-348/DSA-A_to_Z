## check the number is prime or not

def check_prime(num):

    # write your code logic here !!!

    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
