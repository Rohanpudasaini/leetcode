'''
Docstring for amstrong-number.main
Given number is an Amstrong number if the cude of each digit is equal to thr number
example: 
    371 = 3^3 + 7^3 + 1^3
'''

def is_amstrong_number(num:int)-> bool:
    orginal = num
    result = 0
    while num > 0:
        last_digit = num % 10
        result += last_digit**3
        num = num//10
    print(orginal, result)
    return orginal == result

print(is_amstrong_number(371))