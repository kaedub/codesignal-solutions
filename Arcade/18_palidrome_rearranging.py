# Determine if a string can be rearranged to make a palindrome
# 
# Edge Cases: what if odd length and more than one single char?
#             using a set would cause an error
# 
# Strategy: 
# count all items using a dictionary
# 
# remove all even numbers from a values array
# 
# if the length of inputString is even are odd values are none
#   return true
# if the length of inputString is odd and there is only one odd char
#   return true
# else false


def palindromeRearranging(inputString):
    counts = {}
    for c in inputString:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    oddvals = [n for n in counts.values() if n % 2 != 0]
    if len(oddvals) == 1 and len(inputString) % 2 != 0:
        return True
    elif len(oddvals) < 1 and len(inputString) % 2 == 0:
        return True
    return False