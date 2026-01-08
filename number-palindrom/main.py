n=int(input())  
# taking n as a input 
## write your code !!
def reverse_number(n:int) -> int:
    result = 0
    while n > 0:
        last_digit = n % 10
        result = result * 10 + last_digit
        n = n // 10
    return result

if n == reverse_number(n):
    print("true")
else:
    print("false")
