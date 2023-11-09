
def fizz_buzz(n):
    if (n%3 == 0) and (n%5 == 0):
        return 'FizzBuzz'
    elif n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    else:
        return str(n)
    
print(fizz_buzz(15))

'''412. Fizz Buzz - E
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''
    
#Time complexity: O(n) - linear. 
#Space complexity: O(n) because we are creating a list of n elements

def fizz_buzz(n):
    #create an empty list to store the answer
    answer = []
    #loop through the range of 1 to n+1
    for i in range(1, n+1):
        #if i is divisible by 3 and 5, append FizzBuzz to the list
        if (i%3 == 0) and (i%5 == 0):
            answer.append('FizzBuzz')
        #if i is divisible by 3, append Fizz to the list
        elif i%3 == 0:
            answer.append('Fizz')
        elif i%5 == 0:
            answer.append('Buzz')
        #else append the number as a string to the list
        else:
            answer.append(str(i))
    return answer

print(fizz_buzz(15))
