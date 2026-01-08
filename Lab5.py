# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    i = 0
    while i < n:    
        j = 0
        while j < n:
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                result += "*"
            else:
                result += " "
            j += 1
        
        if i != n - 1:
            result += "\n"
        i += 1
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1
        if i != n:
            result += "\n"
        i += 1
    return result 


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    i = 1

    while i <= n:
        # spaces
        j = 0
        while j < n - i:
            result += " "
            j += 1

        # stars
        k = 0
        while k < (2 * i - 1):
            result += "*"
            k += 1

        if i != n:
            result += "\n"

        i += 1

    return result
