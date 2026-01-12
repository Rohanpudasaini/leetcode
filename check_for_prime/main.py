'''
Docstring for check_for_prime.main
Number with two factors, 1 and itself only is prime number
Given number check if its prime or not
'''

# Time complexity O(sqrt N)
def check_prime(num:int) -> bool:
    counter = 0
    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            counter +=2
        if counter > 2:
            return False

    return True

print(check_prime(9999999967))