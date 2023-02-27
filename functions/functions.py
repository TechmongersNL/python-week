# Write a function with one `number` argument that returns double the argument
def double(number: int):
    return number * 2

# Write a function with two `number` arguments that returns double the first argument
def double_first(number1: int, number2: int):
   return number1 * 2

# Write a function with two `number` arguments that returns double the largest argument
def big_double(number1: int, number2: int):
     if number1 > number2:
         return number1 * 2
     else:
         return number2 * 2

# Write a function with a `string` argument and a `number` argument that repeates the string from the first argument but repeated the amount of times equal to the second argument. If the second number is negative, return an empty string
def repeat(text: str, number: int):
    if number < 0: return ""
    return text * number

# Write a function without any arguments. Have it return the string `'na'` repeated 10 times followed by the string `' batman!'`. Use the `repeat` function you used before to accomplish this
def batman():
    na = repeat("na", 10)
    return na + " batman!"

# Write a function with two `number` arguments. Have it return the largest number of the two
def maxi(number1: int, number2: int):
    return max([number1, number2])

# Write a function with two `number` arguments. Have it return the smallest number of the two divided by the largest number
def max_divide(number1: int, number2: int):
    if (number1 > number2):
        return number2 /  number1
    else:
        return number2 / number1

# Write a function with two `string` arguments. Have it return the longest string
def max_string(string1: str, string2: str):
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return string1

# Write a function with a single `number` argument. Return a boolean that indicated wether this number is even
def even(number: int):
    if number % 2 == 0:
        return True
    else:
        return False

# Write a function with a single `number` argument. Return a list of all the positive numbers lower than this argument that are even
def even_below(number: int):
    even_numbers = []

    while number > 0:
        number = number - 1
        if number % 2 == 0:
            even_numbers.append(number)

    return list(reversed(even_numbers))

# Write a function with a single `list of numbers` argument. Return a list of all the numbers in this list that are even
def even_in(numbers: list[int]):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list


# Write a function with a single `list of numbers` argument. Return the result of multiplying all the numbers. If the input contains just 1 number, return that number
def multiply_list(numbers: list[int]):
    multiplied = 1

    for num in numbers:
        multiplied *= num

    return multiplied

# Write a function with a single `list of numbers` argument. Return the result of dividing the number from left to right. So the first number gets divided by the second and the result of that gets divided by the third (and so on..). If the list contains a zero, return zero. If the list contains just one number, return that number
def divide_array(numbers: list[int]):
    numm = numbers[0]

    for num in numbers[1:]:
        if num == 0:
            return 0
        else:
            numm /= num

    return numm

# Write a functions that takes a list of numbers and an argument. Return the average of those numbers
def average(numbers: list[int]):
    return sum(numbers) / len(numbers)

# STEVEN

# Write a function that takes a 'list of numbers' argument. Return the sum of that list multiplied by the length of the array.
def sum_product(numbers: list[int]):
    return sum(numbers) * len(numbers)

# Write a function that capitalizes every other word in a string starting with the first one.
def uppercase_string(string1: str):
    pass

# VIKTORIA

# Write a function that takes a single letter (may be upper or lower case). Return the number of this letter in the English Alphabet.
def alphabet(letter: str):
    diff_letter_ascii = 96
    return ord(letter.lower()) - diff_letter_ascii

# Write a function that takes 2 arguments a text and number of letter in the alphabet. Return the number of times the letter appears in the string (no matter upper or lower case).
def letter_count(text: str, letter_number: int):
    diff_letter_ascii = 96
    letter = chr(letter_number + diff_letter_ascii).lower()
    return text.lower().count(letter.lower())
