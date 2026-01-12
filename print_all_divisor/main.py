'''
Docstring for print_all_divisor.main
find all divisor of number 
'''

# Bruteforce approch
# Time complexity O(N)
def divisor_bruteforce(num:int) -> list[int]:
    result = []
    for i in range(1,num+1):
        if num %i == 0:
            result.append(i)
    return result

# Optimal approach
# Time complexity O(SquartN)
def divisor(num:int) -> list[int]:
    result = []
    for i in range(1, int(num**(1/2))+1):
        if num %i == 0:
            result.append(i)
            if num //i != i:
                result.append(num//i)
    return result



print(divisor_bruteforce(36))
print(divisor(36))