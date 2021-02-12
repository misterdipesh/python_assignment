# Functions
# 1. Write a Python function to find the Max of three numbers.

def maximum_calcutaion (my_list):
    return max(my_list)
print(maximum_calcutaion(1,2,3))
# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def sum_all(my_list):
    return(sum(my_list))
print(sum_all(8, 2, 3, 0, 7))
# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply_all(my_list):
    product=1
    for item in my_list:
        product=product*item
    return product
print(multiply_all(8, 2, 3, -1, 7))
# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def reverse_function (string):
    my_list=list(string)
    my_list.reverse()
    new_string=''
    return (new_string.join(my_list)) 
print(reverse_function("1234abcd"))
# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial_of_number(num):
    if num>0:
        res=1
        for i in range(1,num+1):
            res=res*i
    return res
print(factorial_of_number(3))
# 6. Write a Python function to check whether a number is in a given range.
def test_number_range(num):
    if num in range(1,10):
        return True
    else:
        return False
print(test_number_range(3))
# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def function_to_upper_case(string):
    count_upper=0
    count_lower=0
    for char in string:
        if char.isupper():
            count_upper+=1
        elif char.islower():
            count_lower+=1
    print('No. of Upper case characters:'+str(count_upper))
    print('No. of Lower case Characters:'+str(count_lower))
function_to_upper_case('The quick Brow Fox')

# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(my_list):
    unique=set(my_list)
    return list(unique)
print(unique_list([1,2,3,3,3,3,4,5]))
# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.
def is_prime(num):
    import math
    if num<=1:
        return False
    root_in_int=math.floor(math.sqrt(num))
    for i in range(2,root_in_int):
        if num%i==0:
            return False
    return True
print(is_prime(5))

# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def print_even_num(my_list):
    new_list=[]
    for item in my_list:
        if item%2==0:
            new_list.append(item)
    print(new_list)
print_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.
add_15=lambda a:a+15
print(add_15(4))
multiply=lambda x,y:x*y
print(multiply(2,3))

# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.
def multiply_one_arg(one_num):
    given_num=int(input('given num? ='))
    return given_num*one_num
print(multiply_one_arg(5))
# 13. Write a Python program to sort a list of tuples using Lambda.
sorting_list=given_list.sort(key = lambda x: x[1])
# 14. Write a Python program to sort a list of dictionaries using Lambda.
sorted_dict = sorted(given_dict, key = lambda x: x[1])
# 15. Write a Python program to filter a list of integers using Lambda.
even_nums = list(filter(lambda x: x%2 == 0, nums))
# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.
# using Lambda.
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.
check_string_start=lambda string,character:True if character in string[0] else False
print(check_string_start('hello','h'))


# 18. Write a Python program to check whether a given string is number or not
# using Lambda.
check_string_num=lambda x:True if x in ['1','2','3','4','5','6','7','8','9','0'] else False
print(check_string_num('1'))
# 19. Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
 
Fibonacci_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])

print(Fibonacci_series(2))

# 20. Write a Python program to find intersection of two given arrays using
# Lambda.
array1=1,2,3,4,5,6
array2=2,3,5,9
intersection =list(filter(lambda x: x in array1,array2))
print(intersection)
