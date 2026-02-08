# codewars_solutions.py

# ----------------------------------------
# Challenge 1: Even or Odd
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# ----------------------------------------
def even_or_odd(number):
    """
    Returns 'Even' if number is even, 'Odd' if number is odd.
    """
    return "Even" if number % 2 == 0 else "Odd"


# ----------------------------------------
# Challenge 2: Convert a Number to a String
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8
# ----------------------------------------
def number_to_string(num):
    """
    Converts a number to its string representation.
    """
    return str(num)


# ----------------------------------------
# Challenge 3: Remove String Spaces
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5
# ----------------------------------------
def no_space(x):
    """
    Removes all spaces from the input string.
    """
    return x.replace(" ", "")


# ----------------------------------------
# Challenge 4: Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# ----------------------------------------
def get_count(sentence):
    """
    Counts the number of vowels in the input string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)


# ----------------------------------------
# Example test runs (optional)
# ----------------------------------------
if __name__ == "__main__":
    # Even or Odd
    print(even_or_odd(3)) # Odd
    print(even_or_odd(4)) # Even

    # Number to String
    print(number_to_string(123)) # '123'

    # Remove String Spaces
    print(no_space("Hello World")) # 'HelloWorld'

    # Vowel Count
    print(get_count("abracadabra")) # 5