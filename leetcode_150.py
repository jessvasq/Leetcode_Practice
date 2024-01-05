'''9. Palindrome Number - Easy'''

def isPalindrome(x):
    #check if the number is negative
    if x < 0:
        return False
    #check if the given number is equal to the reverse of the number
    else:
        return str(x) == str(x)[::-1]