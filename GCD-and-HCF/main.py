'''
Docstring for GCD-and-HCF.main
function to find GCD of TWO number
'''

# Time complexity O(min(num1, num2))
def find_GCD(num1:int, num2:int) -> int:
    gcd = 1
    for i in range(1, int(min(num1, num2))+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

# We can also change the loop direction to come from back as it will result in early breaking
# in some case
# Still the time complexity will be same

def find_GCD_reverse(num1:int, num2:int) -> int:
    for i in range(min(num1, num2),0,-1):
        if num1 %i == 0 and num2 % i == 0:
            return i
    return 1

# Time complexity O(max(num1, num2))
# Or precisely O(num1+num2)
def find_GCD_Euclidean(num1:int, num2:int) -> int:
    while num1 != 0:
        num1, num2 = (num1-num2, num2) if num1 > num2 else (num2-num1, num1)
    return num2

# Time complexity O(log(min(num1, num2))) such that num1 and num2 >0
# THis is the most optimal solution as in subtraction we are subtracting little chunks at once, this cause
# the code higher time to converse to zero if two number are far apart
# Rather we are using remainder to reduce the size so that it converse quickly
def find_GCD_Euclidean_Modulo(num1:int, num2:int) -> int:
    while num1 != 0:
        num1, num2 = (num1%num2, num2) if num1 > num2 else (num2%num1, num1)
    return num2

# print(find_GCD(16,32))
print(find_GCD_Euclidean(52,10))