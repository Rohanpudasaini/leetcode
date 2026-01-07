# Write a code to get the last digit from given number

# Example
# Input: 12345, Output: 5

# First method
inp = 12345
out = int(str(inp)[-1])

# Second method without conversion
out = inp % 10


# Write a code to remove last digit
# Example
# Input: 12345 Output:1234

# First method( string conversion )
out = int(str(inp)[:-1])

# Second method
out = inp // 10 # divide by 10 for single digit. If wanted two digit divide by 100 etc

# print(out)

# Write a code to reverse a number without using conversion

def reverse_num(num:int)-> int:
    result = 0
    while True:
        if num == 0:
            break
        digit = num % 10
        num = num // 10
        result= result * 10 + digit

    print(result)

reverse_num(12345)